import streamlit as st
import pandas as pd
import numpy as np
import time
import pickle

cut={'Ideal':4, 'Premium':3, 'Very Good':2, 'Good':1, 'Fair':0}
clarity={'SI1':2, 'IF':7, 'VVS2':5, 'VS1':4, 'VVS1':6, 'VS2':3, 'SI2':1, 'I1':0}
color={'E':1, 'G':3, 'F':2, 'D':0, 'H':4, 'J':6, 'I':5}

st.image("gem/natural_gems.jpg", caption='Image Caption', use_column_width=True)
st.title("Gemstone Price Prediction Appp")
    
pipe=pickle.load(open("gemstonereg.pkl","rb"))


gcut=st.selectbox("Select Gemstone's Cut",sorted(cut.keys()))
gclarity=st.selectbox("Select Gemstone's Carity",sorted(clarity.keys()))
gcolor=st.selectbox("Select Gemstone's Color",sorted(color.keys()))

gcarat=st.number_input("Enter value of Carat between 0.20 to 4.50")


gtable=st.number_input("Enter value of Table between 49 to 79",49,79,57)


gdepth=st.number_input("Enter value of Depth between 59 to 73",59,73,61)

glength=st.number_input("Enter value of lenght between 0 to 10",0,10,5)

gbredth=st.number_input("Enter value of Breadth between 0 to 10",0,59,5)

gheight=st.number_input("Enter value of Height between 0 to 10",0,30,3)

if st.button("Calculate Price"):
    out={
    "carat":[gcarat],
    "cut":[cut[gcut]],
    "color":[color[gcolor]],
    "clarity":[clarity[gclarity]],
    "table":[gtable],
    "depth":[gdepth],
    "x":[glength],
    "y":[gbredth],
    "z":[gheight]
    }
    odf=pd.DataFrame(out)
    st.dataframe(odf)
    st.header(f"Your gemstone price is {pipe.predict(odf)[0]}")

