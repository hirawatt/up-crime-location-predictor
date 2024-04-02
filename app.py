import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import pickle

#with open("./models/random_forest_model.pkl",'rb') as file:
    #loaded_model=pickle.load(file)

def get_user_input():
    numeric_values = [st.sidebar.number_input(f'Enter {col}') for col in ['X', 'Y', 'CENSUS_TRC', 'OCC_DAY', 'OCC_MONTH', 'OCC_YEAR']]
    
    division = st.selectbox('DIVISION', ['Select Division','Central', 'East', 'West'])
    sector_formatted = st.selectbox('SECTOR_FORMATTED', ["Select Sector",'Sector 24','Sector 23',"Sector 21","Sector 25","Sector 31","Sector 13","Sector 14","Sector 21","Sector 32","Sector 22","Sector 33","Sector 34","Sector 35","Sector 17","Sector 16","Sector 15","Sector 36","Sector 12","Sector 11","Sector 37"])
    
    return {
        'SECTOR_FORMATTED': sector_formatted, 
        'DIVISION': division,
        'X': numeric_values[0],
        'Y': numeric_values[1],
        'CENSUS_TRC': numeric_values[2],
        'OCC_DAY': numeric_values[3],
        'OCC_MONTH': numeric_values[4],
        'OCC_YEAR': numeric_values[5]
    }

def main():
    #st.title("Random Forest Model Prediction")
    user_input = get_user_input()
    if st.button('Predict'):
        # Convert user input to DataFrame if your model expects it
        user_input_df = pd.DataFrame([user_input])
        
        # Use the pipeline to preprocess input and make prediction
        prediction = loaded_model.predict(user_input_df)
        st.write(f'Prediction: {prediction}')

if __name__ == '__main__':
    st.set_page_config("Crime Location Predictor",
                        layout="wide",
                        initial_sidebar_state="expanded"
                        )
    st.sidebar.title("Crime Location Predictor")
    st.sidebar.image("./content/OPS.webp")
    c1, c2, c3 = st.columns([4, 4, 1])
    c3.image("./content/OPS.gif", width=150)
    st.title("Crime Location Predictor")
    main()