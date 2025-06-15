# Wimbledon Match Outcome Prediction

This project uses machine learning to predict the outcomes of Wimbledon tennis matches based on player statistics and match history. The model is built using Python, TensorFlow, and pandas.

## Overview
This project trains a neural network model to predict the winner of a tennis match (Player A or Player B) based on:
- Player rankings
- Recent form
- Head-to-head records  

The model preprocesses the data, scales features, and trains a neural network using the `tensorflow` library.

## Features
- **Data Preprocessing**: Converts head-to-head records into numerical features and normalizes input data for better model performance.
- **Custom Neural Network**: A dense feedforward neural network with multiple hidden layers to classify match outcomes.
- **Match Prediction**: Form that takes user-input to predict winners of any match!


## Model Architecture
The model is a sequential neural network with the following layers:

 - Input Layer: Accepts 5 features (player rankings, recent form, and head-to-head record)
 - First Hidden Layer: Dense layer with 64 neurons, ReLU activation, and L2 regularization (0.01)
 - Batch Normalization Layer: Normalizes activations for better training stability
 - Dropout Layer (0.5): Reduces overfitting
 - Second Hidden Layer: Dense layer with 32 neurons, ReLU activation, and L2 regularization (0.01)
 - Batch Normalization Layer: Normalizes activations
 - Dropout Layer (0.5): Reduces overfitting
 - Third Hidden Layer: Dense layer with 16 neurons, ReLU activation, and L2 regularization (0.01)
 - Output Layer: Single neuron with sigmoid activation for binary classification (probability of Player 1 winning)

## Dataset
The dataset contains match data including:

 - Player rankings
 - Recent form (win/loss percentage)
 - Head-to-head records (formatted as wins-losses)
 - Match outcomes (Player A or Player B)

## Results
About 95% accuracy after 50 epochs


