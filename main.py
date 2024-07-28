import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def convert_head_to_head(record):
    if pd.isna(record):
        return 0
    try:
        wins, losses = map(int, record.split('-'))
        return wins - losses  
    except ValueError:
        return 0  


data = pd.read_csv('wimbledon_data.csv')

data['Match Outcome'] = data['Match Outcome'].apply(lambda x: 1 if x == 'Player A' else 0)
data['Head-to-Head Record'] = data['Head-to-Head Record'].apply(convert_head_to_head)

X = data[['Player 1 Ranking', 'Player 2 Ranking', 'Player 1 Recent Form', 'Player 2 Recent Form', 'Head-to-Head Record']]
y = data['Match Outcome']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

y_train = to_categorical(y_train, num_classes=2)
y_test = to_categorical(y_test, num_classes=2)

model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(2, activation='softmax'))


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test loss: {loss:.4f}')
print(f'Test accuracy: {accuracy:.4f}')


