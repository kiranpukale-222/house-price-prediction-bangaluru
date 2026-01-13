import os
import numpy as np
import streamlit as st
import pickle 
import json


st.set_page_config(
    page_title="Bangaluru House-Price Prediction",
    page_icon="🏡",
    layout= "centered"
    )
## main title
st.markdown(
    "<h1 style='text-align:center;'>🏡Bangaluru House-Price Prediction</h1>",
    unsafe_allow_html=True
    )

try:
     ## Base directory (folder where app.py is placed)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        ## load columns  ## r- read filein application
    with open (os.path.join(BASE_DIR,"columns.json"),"r") as f:    
        data_columns = json.load(f)["data_columns"]

        ### location column start from index 3
    locations = data_columns[3:] 

        ### load model  ##'rb'-read binary
    with open (os.path.join(BASE_DIR,"Bangaluru_house _price_pred.pickle"),'rb') as f:
        model = pickle.load(f)

    ### stored list of bath and bhk list used as "Dropdown values"
    bhk_list = sorted([ 4,  3,  2,  5,  1,  6,  8,  7,  9, 11, 16, 10, 13])
    bath_list = sorted([ 4.,  3.,  2.,  5.,  1.,  6.,  8.,  7.,  9., 16., 12., 13.])

        ## inputs
    total_sqft = st.number_input("Total Square Feet",min_value=300)
    bhk = st.selectbox("BHK",bhk_list)
    bath = st.selectbox("Bath",bath_list)
    location = st.selectbox("Location",locations)

        ## prediction
    if st.button("Estimate Price"):
        p = np.zeros(len(data_columns))
        p[0] = total_sqft
        p[1] = bath
        p[2] = bhk

        if location.lower() in data_columns:
            loc_index = data_columns.index(location.lower())
            p[loc_index] = 1

        price = model.predict([p])[0]
        st.success(f"Estimated Price: ₹ {round(price,2)} Lakhs")

except Exception as e:
    st.error("App crashed due to this error")
    st.exception(e)