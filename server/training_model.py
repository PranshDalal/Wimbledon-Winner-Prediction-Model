import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2

df = pd.read_csv('synthetic_wimbledon_matches.csv')

def convert_head_to_head(record):
    if pd.isna(record):
        return 0
    try:
        wins, losses = map(int, record.split('-'))
        return wins - losses  
    except ValueError:
        return 0
    
df['Head-to-Head Record'] = df['Head-to-Head Record'].apply(convert_head_to_head)

X = df[['Player 1 Ranking', 'Player 2 Ranking', 'Player 1 Form', 'Player 2 Form', 'Head-to-Head Record']]
y = df.apply(lambda row: 1 if row['Match Outcome'] == row['Player 1'] else 0, axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],), kernel_regularizer=l2(0.01)),
    BatchNormalization(),
    Dropout(0.5),
    Dense(32, activation='relu', kernel_regularizer=l2(0.01)),
    BatchNormalization(),
    Dropout(0.5),
    Dense(16, activation='relu', kernel_regularizer=l2(0.01)),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_split=0.2)

y_pred = (model.predict(X_test_scaled) > 0.5).astype("int32")
print(classification_report(y_test, y_pred, target_names=['Player 2 Wins', 'Player 1 Wins']))

model.save('wimbledon_match_predictor.h5')
import pickle
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)






