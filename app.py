import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import pickle

st.set_page_config("Crime Location Predictor",
                    layout="wide",
                    initial_sidebar_state="expanded"
                    )
try:
    with open("./models/Assaults.pkl",'rb') as file:
        loaded_model=pickle.load(file)
except:
    st.info("Running on cloud. Unable to run models")

def get_user_input(tab):
    if (tab==1):
        numeric_values = [st.sidebar.number_input(f'Enter {col}', key=f"nv{tab}{col}", disabled=distab1) for col in ['X', 'Y', 'CENSUS_TRC', 'OCC_DAY', 'OCC_MONTH', 'OCC_YEAR']]
        division = st.sidebar.selectbox('DIVISION', ['Select Division','Central', 'East', 'West'], key=f"division{tab}", disabled=distab1)
        sector = st.sidebar.selectbox('SECTOR_FORMATTED', ["Select Sector",'Sector 24','Sector 23',"Sector 21","Sector 25","Sector 31","Sector 13","Sector 14","Sector 21","Sector 32","Sector 22","Sector 33","Sector 34","Sector 35","Sector 17","Sector 16","Sector 15","Sector 36","Sector 12","Sector 11","Sector 37"], key=f"sector{tab}", disabled=distab1)
        return {
        'SECTOR_FORMATTED': sector, 
        'DIVISION': division,
        'X': numeric_values[0],
        'Y': numeric_values[1],
        'CENSUS_TRC': numeric_values[2],
        'OCC_DAY': numeric_values[3],
        'OCC_MONTH': numeric_values[4],
        'OCC_YEAR': numeric_values[5]
        }

    elif (tab==2):
        numeric_values = [st.sidebar.number_input(f'Enter {col}', key=f"nv{tab}{col}", disabled=distab2) for col in ['X', 'Y', 'CENSUS_TRC', 'OCC_DAY', 'OCC_MONTH', 'OCC_YEAR']]
        division = st.sidebar.selectbox('DIVISION', ['Select Division','Central', 'East', 'West'], key=f"division{tab}", disabled=distab2)
        sector = st.sidebar.selectbox('SECTOR_FORMATTED', ["Select Sector",'Sector 24','Sector 23',"Sector 21","Sector 25","Sector 31","Sector 13","Sector 14","Sector 21","Sector 32","Sector 22","Sector 33","Sector 34","Sector 35","Sector 17","Sector 16","Sector 15","Sector 36","Sector 12","Sector 11","Sector 37"], key=f"sector{tab}", disabled=distab2)
        return {
            'SECTOR_FORMATTED': sector, 
            'DIVISION': division,
            'X': numeric_values[0],
            'Y': numeric_values[1],
            'CENSUS_TRC': numeric_values[2],
            'OCC_DAY': numeric_values[3],
            'OCC_MONTH': numeric_values[4],
            'OCC_YEAR': numeric_values[5]
        }
    elif (tab==3):
        numeric_values = [st.sidebar.number_input(f'Enter {col}', key=f"nv{tab}{col}", disabled=distab3) for col in ['X', 'Y', 'CENSUS_TRC', 'OCC_DAY', 'OCC_MONTH', 'OCC_YEAR']]
        division = st.sidebar.selectbox('DIVISION', ['Select Division','Central', 'East', 'West'], key=f"division{tab}", disabled=distab3)
        sector = st.sidebar.selectbox('SECTOR_FORMATTED', ["Select Sector",'Sector 24','Sector 23',"Sector 21","Sector 25","Sector 31","Sector 13","Sector 14","Sector 21","Sector 32","Sector 22","Sector 33","Sector 34","Sector 35","Sector 17","Sector 16","Sector 15","Sector 36","Sector 12","Sector 11","Sector 37"], key=f"sector{tab}", disabled=distab3)

        bike_style = st.sidebar.selectbox('BIKE_STYLE', ['STOLEN','RECOVERED', 'FOUND', 'SEIZED', 'LOST','COUNTERFEIT'], disabled=distab3)
        bike_type = st.sidebar.selectbox('BIKE_TYPE', ['HYBRID','MOUNTAIN', 'REGULAR', 'OTHER', 'TOURING','BMX','RACER', ], disabled=distab3)
        bike_frame = st.sidebar.selectbox('BIKE_FRAME', ["MEN'S","WOMEN'S", 'UNISEX', "CHILD'S"], disabled=distab3)
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
    else:
        st.error("Error selecting tab")

distab1, distab2, distab3 = False, False, False

def run_predictor():
    #tab1, tab2, tab3, tab4 = st.tabs(["Assaults", "Theft Under 5000", "Bike Theft", "All"])
    crime_type = st.radio("Select Crime Type", ["Assaults", "Theft Under 5000", "Bike Theft", "All"], horizontal=True)
    if crime_type=="Assaults":
        distab1, distab2, distab3 = False, True, True
        st.sidebar.subheader("Assaults Input")
        user_input = get_user_input(1)
        if st.sidebar.button('Predict'):
            user_input_df = pd.DataFrame([user_input])
            prediction = loaded_model.predict(user_input_df)
            st.write(f'Prediction: {prediction}')
    
    elif crime_type=="Theft Under 5000":
        distab1, distab2, distab3 = True, False, True
        st.sidebar.subheader("Theft Under 5000 Input")
        user_input = get_user_input(2)
        if st.sidebar.button('Predict'):
            user_input_df = pd.DataFrame([user_input])
            prediction = loaded_model.predict(user_input_df)
            st.write(f'Prediction: {prediction}')

    elif crime_type=="Bike Theft":
        distab1, distab2, distab3 = True, True, False
        st.sidebar.subheader("Bike Theft Input")
        user_input = get_user_input(3)
        if st.sidebar.button('Predict'):
            user_input_df = pd.DataFrame([user_input])
            prediction = loaded_model.predict(user_input_df)
            st.write(f'Prediction: {prediction}')
    
    elif crime_type=="All":
        st.info("Unified Map of All Data")

def main():
    st.sidebar.title("Crime Location Predictor")
    st.sidebar.image("./content/OPS.webp", width=100)
    c2, c3 = st.columns([18, 2])
    c2.image("./content/OPS blue.gif", use_column_width=True)
    c3.image("./content/OPS.gif", width=100)
    st.title("Crime Location Predictor")

    with st.expander("About the app"):
        st.write("Crime Location Predictor")
    try:
        run_predictor()
    except:
        st.info("Running on cloud. Unable to run models")

if __name__ == '__main__':
    main()