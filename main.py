import streamlit as st
import pandas as pd
import matplotlib.pylab as plt


st.title('Simple Data Dashboard')

uploaded_file = st.file_uploader("Choose a csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader('Data Preview')
    st.write(df.head(10))
    
    st.subheader('Data Summary')
    st.write(df.describe())
    
    st.subheader('Data Filter')
    columns = df.columns.tolist()
    selected_column = st.selectbox('Select Columns', columns)
    
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox('Select Values', unique_values)
    
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)
    
    st.subheader('Plot Data')
    x_column = st.selectbox('Select X-axis Column', columns)
    y_column = st.selectbox('Select Y-axis Column', columns)
    
    if st.button('Generate Plot'):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write('Please upload a csv file')