import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = {
    'PlayerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Jannik Sinner', 'Novak Djokovic', 'Carlos Alcaraz', 'Alexander Zverev', 'Daniil Medvedev', 'Andrey Rublev', 'Hubert Hurkacz', 'Casper Ruud', 'Alex de Minaur', 'Grigor Dimitrov'],
    'Age': [22, 33, 21, 23, 24, 26, 27, 25, 24, 32],
    'Height': [188, 188, 185, 198, 198, 188, 196, 185, 183, 192],
    'Weight': [77, 77, 80, 90, 83, 82, 89, 80, 78, 85],
    'Country': ['Italy', 'Serbia', 'Spain', 'Germany', 'Russia', 'Russia', 'Poland', 'Norway', 'Australia', 'Bulgaria'],
    'Rank': [10, 1, 2, 7, 8, 9, 12, 14, 15, 20],
    'Seeding': [10, 1, 2, 7, 8, 9, 12, 14, 15, 20],
    'MatchesPlayed': [52, 52, 45, 42, 45, 40, 38, 44, 41, 36],
    'MatchesWon': [38, 45, 35, 33, 36, 32, 28, 30, 27, 29],
    'Aces': [480, 520, 490, 420, 460, 405, 410, 400, 395, 370],
    'DoubleFaults': [60, 45, 52, 47, 49, 48, 50, 53, 55, 50],
    'FirstServePercentage': [68, 67, 69, 62, 65, 64, 66, 61, 63, 60],
    'BreakPointsConverted': [42, 44, 39, 43, 37, 41, 38, 40, 36, 34],
    'NetPointsWon': [70, 72, 68, 67, 73, 69, 66, 70, 65, 64],
    'WinStreak': [8, 12, 10, 7, 9, 6, 5, 7, 4, 6],
    'WinProbability': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
}

df = pd.DataFrame(data)

X = df.drop(columns=['PlayerID', 'Name', 'Country', 'WinProbability'])
y = df['WinProbability']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = Sequential([
    Dense(16, input_dim=X_train.shape[1], activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=50, batch_size=1, verbose=1)

loss, accuracy = model.evaluate(X_test, y_test)

y_pred = (model.predict(X_test) > 0.5).astype(int)

print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{classification_report(y_test, y_pred)}')
