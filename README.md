# Wimbledon Match Outcome Prediction

This project uses machine learning to predict the outcomes of Wimbledon tennis matches based on player statistics and match history. The model is built using Python, TensorFlow, and pandas.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Dataset](#dataset)
- [Results](#results)

---

## Overview
This project trains a neural network model to predict the winner of a tennis match (Player A or Player B) based on:
- Player rankings
- Recent form
- Head-to-head records  

The model preprocesses the data, scales features, and trains a neural network using the `tensorflow` library.

---

## Features
- **Data Preprocessing**: Converts head-to-head records into numerical features and normalizes input data for better model performance.
- **Custom Neural Network**: A dense feedforward neural network with multiple hidden layers to classify match outcomes.
- **Performance Metrics**: Outputs loss and accuracy to evaluate model performance.

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/PranshDalal/TennisPrediction
   cd TennisPrediction
2. Install the required libraries:

## Usage
1. Run main.py
   ```bash
   python main.py

## Model Architecture
The model is a sequential neural network with the following layers:

 - Input Layer: Accepts 5 features (player rankings, recent form, and head-to-head record).
 - Hidden Layers: Two dense layers with 64 and 32 neurons, using ReLU activation.
 - Output Layer: A softmax layer with 2 neurons (binary classification for Player A or Player B).

## Dataset
The dataset contains match data, including:

 - Player rankings
 - Recent form (win/loss percentage)
 - Head-to-head records (formatted as wins-losses)
 - Match outcomes (Player A or Player B)

## Results
About 80% accuracy after 20 epochs


