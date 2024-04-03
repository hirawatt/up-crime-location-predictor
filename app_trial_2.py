import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64



with open("Assaults.pkl", 'rb') as file:
    loaded_model = pickle.load(file)

# Latitude and longitude of Ottawa
ottawa_latitude = 45.4215
ottawa_longitude = -75.6972

def main():
    st.sidebar.image("C:\\Users\\ayesh\\Downloads\\OPS.jpg", width=200)
    st.sidebar.title("Crime Prediction")

    numeric_values = [
        st.sidebar.number_input(f'Enter {col}') for col in ['X', 'Y', 'CENSUS_TRC', 'OCC_DAY', 'OCC_MONTH', 'OCC_YEAR']
    ]
    division = st.sidebar.selectbox('DIVISION', ['Select Division','Central', 'East', 'West'])
    sector_formatted = st.sidebar.selectbox(
        'SECTOR_FORMATTED',
        ["Select Sector",'Sector 24','Sector 23',"Sector 21","Sector 25","Sector 31","Sector 13","Sector 14","Sector 21","Sector 32","Sector 22","Sector 33","Sector 34","Sector 35","Sector 17","Sector 16","Sector 15","Sector 36","Sector 12","Sector 11","Sector 37"]
    )

    user_input = {
        'SECTOR_FORMATTED': sector_formatted,
        'DIVISION': division,
        'X': numeric_values[0],
        'Y': numeric_values[1],
        'CENSUS_TRC': numeric_values[2],
        'OCC_DAY': numeric_values[3],
        'OCC_MONTH': numeric_values[4],
        'OCC_YEAR': numeric_values[5]
    }

    # Add the GIF at the top
    st.image(r"C:\Users\ayesh\Downloads\Untitled design (9).gif", use_column_width=True)
    # GIF File

    


    st.title("Crime Location Predictor")

    with st.expander("About the app"):
        st.write("Crime Location Predictor")

    tabs = ["Assaults", "Theft Under 5000", "Bike Theft"]
    selected_tab = st.sidebar.radio("Select a tab", tabs)

    if selected_tab == "Assaults":
        if st.sidebar.button('Predict'):
            try:
                # Convert user input to DataFrame if your model expects it
                user_input_df = pd.DataFrame([user_input])

                # Use the pipeline to preprocess input and make prediction
                prediction = loaded_model.predict(user_input_df)

                # Convert prediction to scalar if it's a NumPy array
                prediction_scalar = prediction.item() if isinstance(prediction, np.ndarray) else prediction

                # Display the prediction
                st.write(f'Prediction: {prediction_scalar}')

                # Create DataFrame for Ottawa location
                ottawa_data = pd.DataFrame({'LATITUDE': [ottawa_latitude], 'LONGITUDE': [ottawa_longitude]})

                # Create DataFrame for predicted location
                predicted_data = pd.DataFrame({'LATITUDE': [user_input['X']], 'LONGITUDE': [user_input['Y']], 'PREDICTION': [prediction_scalar]})

                # Visualize Ottawa and predicted location on a map
                st.map(ottawa_data)
                
                # Display assault emoji on the map for predicted location
                st.write(f"Assault location: Latitude - {user_input['X']}, Longitude - {user_input['Y']}")

            except Exception as e:
                st.error(f"Error in main: {e}")

    # Add similar blocks for other tabs like "Theft Under 5000" and "Bike Theft" if needed
    
    


if __name__ == '__main__':
    main()
