from mase_test import mase, preprocess
import streamlit as st
import os



st.title('MASE Testing')

file = st.selectbox("What file would you like to use?", os.listdir('data'))

processed = preprocess(file)

to_plt = mase(processed)
st.write(to_plt)

