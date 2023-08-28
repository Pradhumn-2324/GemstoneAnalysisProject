import streamlit as st
import pandas as pd
import seaborn as sns


df=pd.read_csv("cubic_zirconia.csv")

st.title("my first streamlit app")

st.dataframe(df.head(10))

sns.set(style="darkgrid")
ax = sns.countplot(x='cut',data=df)

    # Display the countplot in Streamlit app
st.pyplot(ax.figure)
