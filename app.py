import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import pickle
import base64

# GIF File
file_ = open("./content/OPS.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

with open("./models/Assaults.pkl",'rb') as file:
    loaded_model=pickle.load(file)

def get_user_input(tab):
    if (tab==1):
        numeric_values = [st.sidebar.number_input(f'Enter {col}', key=f"nv{tab}{col}") for col in ['X', 'Y', 'CENSUS_TRC', 'OCC_DAY', 'OCC_MONTH', 'OCC_YEAR']]
        division = st.sidebar.selectbox('DIVISION', ['Select Division','Central', 'East', 'West'], key=f"division{tab}")
        sector = st.sidebar.selectbox('SECTOR_FORMATTED', ["Select Sector",'Sector 24','Sector 23',"Sector 21","Sector 25","Sector 31","Sector 13","Sector 14","Sector 21","Sector 32","Sector 22","Sector 33","Sector 34","Sector 35","Sector 17","Sector 16","Sector 15","Sector 36","Sector 12","Sector 11","Sector 37"], key=f"sector{tab}")
        st.sidebar.divider()
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
        numeric_values = [st.sidebar.number_input(f'Enter {col}', key=f"nv{tab}{col}") for col in ['X', 'Y', 'CENSUS_TRC', 'OCC_DAY', 'OCC_MONTH', 'OCC_YEAR']]
        division = st.sidebar.selectbox('DIVISION', ['Select Division','Central', 'East', 'West'], key=f"division{tab}")
        sector = st.sidebar.selectbox('SECTOR_FORMATTED', ["Select Sector",'Sector 24','Sector 23',"Sector 21","Sector 25","Sector 31","Sector 13","Sector 14","Sector 21","Sector 32","Sector 22","Sector 33","Sector 34","Sector 35","Sector 17","Sector 16","Sector 15","Sector 36","Sector 12","Sector 11","Sector 37"], key=f"sector{tab}")
        st.sidebar.divider()
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
        numeric_values = [st.sidebar.number_input(f'Enter {col}', key=f"nv{tab}{col}") for col in ['X', 'Y', 'CENSUS_TRC', 'OCC_DAY', 'OCC_MONTH', 'OCC_YEAR']]
        division = st.sidebar.selectbox('DIVISION', ['Select Division','Central', 'East', 'West'], key=f"division{tab}")
        sector = st.sidebar.selectbox('SECTOR_FORMATTED', ["Select Sector",'Sector 24','Sector 23',"Sector 21","Sector 25","Sector 31","Sector 13","Sector 14","Sector 21","Sector 32","Sector 22","Sector 33","Sector 34","Sector 35","Sector 17","Sector 16","Sector 15","Sector 36","Sector 12","Sector 11","Sector 37"], key=f"sector{tab}")

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
    else:
        st.error("Error selecting tab")

def run_predictor():
    tab1, tab2, tab3 = st.tabs(["Assaults", "Theft Under 5000", "Bike Theft"])
    with tab1:
        st.sidebar.subheader("Assaults Input")
        user_input = get_user_input(1)
        if st.sidebar.button('Predict'):
            # Convert user input to DataFrame if your model expects it
            user_input_df = pd.DataFrame([user_input])
            
            # Use the pipeline to preprocess input and make prediction
            prediction = loaded_model.predict(user_input_df)
            st.write(f'Prediction: {prediction}')
    
    with tab2:
        user_input = get_user_input(2)

    with tab3:
        user_input = get_user_input(3)

def main():
    st.set_page_config("Crime Location Predictor",
                        layout="wide",
                        initial_sidebar_state="expanded"
                        )
    st.sidebar.title("Crime Location Predictor")
    st.sidebar.image("./content/OPS.webp", width=100)
    c2, c3 = st.columns([3, 2])
    c2.video("https://youtu.be/3boD9s0oDck")
    c3.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="OPS gif">',
    unsafe_allow_html=True,
    )
    st.title("Crime Location Predictor")

    with st.expander("About the app"):
        st.write("Crime Location Predictor")
    #run_predictor()

if __name__ == '__main__':
    main()