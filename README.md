
# Insurance Cost Prediction

![gif_sped](https://github.com/g-gourav-r/Insurance-Cost-Predictor/assets/75977813/863f5535-a4cd-41b6-92d6-298dd73543c5)

## Basic Workflow

[insurance.csv] --> [model_training.ipynb] --> [trained_model.sav] (Using Pickle) --> [webapp.py] (Streamlit Web App Using the Model)


This repository contains code for predicting insurance costs using a linear regression model.

## Files in this Repository

1. **insurance.csv**:
   - This file contains the dataset used for training and testing the insurance cost prediction model.
   - It includes various features such as age, sex, BMI, number of children, smoking status, and region, along with the target variable, insurance charges.
   - This dataset is used in the `model_training.ipynb` file for training the machine learning model.

2. **model_training.ipynb**:
   - This Jupyter Notebook file contains the code for training the insurance cost prediction model.
   - It loads the 'insurance.csv' dataset, performs data analysis and preprocessing, including encoding categorical features.
   - The notebook then splits the data into training and testing sets, trains a linear regression model, and saves the trained model as 'trained_model.sav'.
   - Additionally, it provides evaluation metrics such as R-squared on both the training and testing data.

3. **trained_model.sav**:
   - This file contains the saved machine learning model that was trained using the 'model_training.ipynb' script.
   - It is a binary file that stores the model's parameters and can be loaded to make predictions without retraining.

4. **webapp.py**:
   - This Python script likely represents a web application or API for making insurance cost predictions using the trained model.
   - It probably uses a web framework like Flask or Django to serve the model.
   - Users can interact with the web application by providing input data in the format `(age, sex, bmi, children, smoker, region)` to receive insurance cost predictions.

## Usage

1. **Training the Model**:

   To train the linear regression model and save it, refer to the `model_training.ipynb` notebook for details.

2. **Making Predictions**:

   To load the saved model and make predictions on new data, use the 'webapp.py' script. You may need to deploy it as a web application.

   Provide input data in the format `(age, sex, bmi, children, smoker, region)` to get predictions for insurance costs.

## Example Input

Input data for predictions should be provided as a tuple in the format `(age, sex, bmi, children, smoker, region)`.

## Prerequisites

- Python 3.x
- Libraries: numpy, pandas, matplotlib, seaborn, scikit-learn
