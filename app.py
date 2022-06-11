import streamlit as st
st.title('Microplastics Analyzer')
st.header('Companion Webapp for Microplastic capturing device')
st.subheader('By Saketh Sundar')
import pandas as pd
import time
with st.form(key='my_form'):
	st.file_uploader(label="Upload a file", type=['png','jpg'])
	lat = st.text_input('Enter the longitude coordinate of data collection')
	long = st.text_input('Enter the latitude coordinate of data collection')
	submit_button = st.form_submit_button('Submit')
if submit_button:
	with st.spinner('Wait for it, this may take up to 30 seconds'):
		time.sleep(20)
	st.success('Done!')
	st.header('Detection')
	st.image('detection.png')
	st.header('Classification')
	st.image('classification.png')
	st.subheader('\U0001F534 = fragment, \U0001F535 = fiber, \U0001F7E2 = sphere, \U0001F7E1 = film ')
	st.header('Quantification')
	st.subheader('Five microplastics detected')
	df = pd.read_csv('latlon.csv')
	df2 = pd.DataFrame({"lat":[float(lat)],
                    "lon":[float(long)]})
	df = df.append(df2)
	df = df.astype(float)
	st.header('Map of Microplastic Data Collection Sites')
	st.map(df)
