import streamlit as st
import pandas as pd
import pickle
import requests

# Load the trained DecisionTreeRegressor model
with open('insurane_predictor_dtr.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to predict insurance charges
def predict_charges(age, bmi, children, smoker, sex):
    input_data = {'age': age, 'bmi': bmi, 'children': children, 'smoker': smoker, 'sex': sex}
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    return prediction

# Function to convert charges to different currencies
def convert_to_currencies(charges_in_usd):
    currency_symbols = {'INR': '₹', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'AUD': 'A$'}
    exchange_rates = {}

    # API for currency exchange rates (using exchangeratesapi.io)
    api_url = 'https://open.er-api.com/v6/latest'
    params = {'base': 'USD'}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        exchange_rates = data['rates']

    converted_charges = {currency: charges_in_usd * exchange_rates.get(currency, 1) for currency in currency_symbols}
    return converted_charges

# Streamlit App
def main(currency_symbols=None):
    st.title('Medical Insurance Predictor')

    # Input widgets
    age = st.slider('Select Age', min_value=18, max_value=64, value=30)
    bmi = st.slider('Select BMI', min_value=15.0, max_value=50.0, value=25.0)
    children = st.slider('Select Number of Children', min_value=0, max_value=5, value=0)
    smoker = st.radio('Are you a Smoker?', ('No', 'Yes'))
    sex = st.radio('Select Gender', ('Male', 'Female'))

    # Convert categorical inputs to numerical
    smoker = 1 if smoker == 'Yes' else 0
    sex = 1 if sex == 'Female' else 0

    # Make prediction
    if st.button('Predict Insurance Charges'):
        prediction_in_usd = predict_charges(age, bmi, children, smoker, sex)
        st.success(f'Predicted Insurance Charges (USD): ${prediction_in_usd:.2f}')

        # Convert to different currencies
        converted_charges = convert_to_currencies(prediction_in_usd)

        # Display converted charges
        st.write('Converted Charges:')
        for currency, charge in converted_charges.items():
            st.write(f'{currency}: {charge:.2f} {currency_symbols[currency]}')
if __name__ == '__main__':
    currency_symbols = {'INR': '₹', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'AUD': 'A$'}
    main(currency_symbols)
