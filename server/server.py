from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

model = load_model('wimbledon_match_predictor.h5')
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or not all(key in data for key in ['Player 1 Ranking', 'Player 2 Ranking', 'Player 1 Form', 'Player 2 Form', 'Head-to-Head Record']):
        return jsonify({'error': 'Invalid input data'}), 400

    def convert_head_to_head(record):
        if pd.isna(record):
            return 0
        try:
            wins, losses = map(int, record.split('-'))
            return wins - losses  
        except ValueError:
            return 0

    head_to_head = convert_head_to_head(data['Head-to-Head Record'])
    
    features = np.array([[data['Player 1 Ranking'], data['Player 2 Ranking'], 
                          data['Player 1 Form'], data['Player 2 Form'], 
                          head_to_head]])
    
    features_scaled = scaler.transform(features)
    
    prediction = model.predict(features_scaled)
    outcome = 'Player 1 Wins' if prediction[0][0] > 0.5 else 'Player 2 Wins'
    
    return jsonify({'prediction': outcome, 'probability': float(prediction[0][0])})

if __name__ == '__main__':
    app.run(debug=True)