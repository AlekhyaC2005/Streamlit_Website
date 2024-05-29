import streamlit as st
import numpy as np
import pandas as pd

import seaborn as sns
try:
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6; /* Set your desired background color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('Sales Data Analysis Website')
    st.header('This Website is created by Group-36')
    st.subheader('Hello!!')
    st.markdown('------')
    path = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in path:
       uploaded_file = pd.read_csv(uploaded_file)
       uploaded_file
  # Perform data analysis
    st.write('## EDA')
    st.write(uploaded_file.describe())
    st.write(uploaded_file.info())
    st.subheader('Null Values')
    st.write(uploaded_file.isnull().sum())

# Replace null values with mean for integer columns
    numeric_columns = uploaded_file.select_dtypes(include=['int', 'float']).columns
    filled_data = uploaded_file.copy()
    for col in numeric_columns:
            if filled_data[col].isnull().any():  # Check if there are null values in the column
                filled_data[col].fillna(filled_data[col].mean(), inplace=True)

        # Display the filled data
    st.subheader("Data with Null Values Replaced by Mean")
    st.write(filled_data)

    # Plot 
    fig, (ax1,ax2) = plt.subplots(2)
    column = st.selectbox('Select a column for histogram:', uploaded_file.columns)
    ax1.hist(uploaded_file[column], bins=20,color='g',edgecolor='r')
    ax2.plot(uploaded_file[column],marker='o',markersize=4,markerfacecolor='red')
    st.pyplot(fig)
# Scatter plot
    st.subheader("Scatter Plot")
    x_axis = st.selectbox("Select X-axis", uploaded_file.columns)
    y_axis = st.selectbox("Select Y-axis", uploaded_file.columns)
    fig1, ax = plt.subplots()
    plt.scatter(uploaded_file[x_axis], uploaded_file[y_axis], alpha=0.5,color='r')
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig1)

    column = st.selectbox("Select column for boxplot", uploaded_file.columns)

# Create boxplot
    st.subheader("Boxplot")
    fig2, ax = plt.subplots()
    plt.boxplot(uploaded_file[column],whiskerprops={'color':'b'})
    plt.xlabel(column)
    plt.ylabel("Value")
    st.pyplot(fig2)

 

    column = st.selectbox("Select column for stem plot", uploaded_file.columns)

        # Create stem plot
    st.subheader("Stem Plot")
    fig3, ax = plt.subplots()
    plt.stem(uploaded_file[column],markerfmt='go',linefmt='orangered',orientation='horizontal')
    plt.xlabel("Index")
    plt.ylabel("Value")
    st.pyplot(fig3)

    fig4, ax3 = plt.subplots()
    columns = st.multiselect("Select columns for step plot", uploaded_file.columns)
    if columns:
            # Create step plot
            st.subheader("Step Plot",'Stack Plot')
            for col in columns:
                #plt.step(uploaded_file.index, uploaded_file[col], label=col)
                plt.stackplot(range(len(uploaded_file)), [uploaded_file[col] for col in columns], labels=columns)
            plt.xlabel("Index")
            plt.ylabel("Value")
            plt.legend()
            st.pyplot(fig4)

except NameError:
    st.write("Please Enter a CSV File")
