from mase_test import mase, preprocess
import streamlit as st
import os
import pandas as pd



st.title('MASE Testing')

toggle = st.toggle("Upload your own file?")
if toggle:
    file = st.file_uploader("Upload a file")
    if file:
        processed = preprocess(pd.read_csv(file,index_col=0),isframe=True)
        to_plt = mase(processed)
        st.write(to_plt)
else:
    file = st.selectbox("What file would you like to use?", os.listdir('data'))

    processed = preprocess(file)

    to_plt = mase(processed)
    st.write(to_plt)

