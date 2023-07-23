import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
option = st.selectbox(
        'Which Model to Use?',
        ('Multiple Linear Regression.sav', 'Support Vector Machine.sav', 'Random Forest Regressor.sav'))

st.write('You selected:', option)
model = pickle.load(open(option, 'rb'))

st.title('House price Prediction')
st.sidebar.header('House Data')
image = Image.open('bb.jpg')
st.image(image, '')

# FUNCTION
def user_report():
  House_Age = st.sidebar.slider('House Age', 0,45, 0 )
  Nearest_Metro = st.sidebar.slider('Nearest Metro (km)', 20,1000, 10 )
  Convenience_stores = st.sidebar.slider('Convenience stores', 0,10, 1 )
  Latitude = st.sidebar.slider('Latitude', 24.0,25.0, 24.0 )
  Longitude = st.sidebar.slider('longitude', 121.4735,121.56627, 121.4730)

  user_report_data = {
      'House Age':House_Age,
      'Distance from nearest Metro station (km)':Nearest_Metro,
      'Number of convenience stores':Convenience_stores,
      'latitude':Latitude,
      'longitude':Longitude,
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data

user_data = user_report()
st.header('House Data')
st.write(user_data)

Price = model.predict(user_data)
st.subheader('House Price Per Unit Area')
st.subheader('$'+str(np.round(abs(Price[0]), 2)))
