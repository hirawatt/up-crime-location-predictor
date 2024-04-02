import sklearn
import streamlit as st
import pandas as pd   
import pickle

with open("./Bike_theft_new.pkl",'rb') as file:
    loaded_model=pickle.load(file)

def get_user_input():
    numeric_values = [st.sidebar.number_input(f'Enter {col}', key=f"nv{col}") for col in ['X', 'Y', 'CENSUS_TRC', 'OCC_DAY', 'OCC_MONTH', 'OCC_YEAR']]
    division = st.sidebar.selectbox('DIVISION', ['Select Division','Central', 'East', 'West'], key=f"division")
    sector = st.sidebar.selectbox('SECTOR_FORMATTED', ["Select Sector",'Sector 24','Sector 23',"Sector 21","Sector 25","Sector 31","Sector 13","Sector 14","Sector 21","Sector 32","Sector 22","Sector 33","Sector 34","Sector 35","Sector 17","Sector 16","Sector 15","Sector 36","Sector 12","Sector 11","Sector 37"], key=f"sector")

    bike_style = st.sidebar.selectbox('BIKE_STYLE', ['STOLEN','RECOVERED', 'FOUND', 'SEIZED', 'LOST','COUNTERFEIT' ])
    bike_type = st.sidebar.selectbox('BIKE_TYPE', ['HYBRID','MOUNTAIN', 'REGULAR', 'OTHER', 'TOURING','BMX','RACER', ])
    bike_frame = st.sidebar.selectbox('BIKE_FRAME', ["MEN'S","WOMEN'S", 'UNISEX', "CHILD'S"])
    st.sidebar.divider()
    return {
        'SECTOR': sector,
        'BIKE_STYLE': bike_style,
        'BIKE_TYPE': bike_type,
        'BIKE_FRAME': bike_frame,
        'DIVISION': division,
        'X': numeric_values[0],
        'Y': numeric_values[1],
        'CENSUS_TRC': numeric_values[2],
        'OCC_DAY': numeric_values[3],
        'OCC_MONTH': numeric_values[4],
        'OCC_YEAR': numeric_values[5]
    }

def main():
    st.title("Random Forest Model Prediction")
    user_input = get_user_input()
    if st.sidebar.button('Predict'):
        # Convert user input to DataFrame if your model expects it
        user_input_df = pd.DataFrame([user_input])
        
        # Use the pipeline to preprocess input and make prediction
        prediction = loaded_model.predict(user_input_df)
        st.write(f'Prediction: {prediction}')

if __name__ == '__main__':
    main()

