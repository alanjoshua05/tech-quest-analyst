import streamlit as st
import pandas as pd
import openpyxl

st.title('Tech Quest Data Analyst')

file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])
a = st.text_input("Select the column to be analysed (ex: E-mail)")
sub = st.button('Analayse')

if sub:
    if file is not None:
        st.subheader("The results")
        try:
            df1 = pd.read_excel("Csbs.xlsx")  # Pre-existing data
            df2 = pd.read_excel(file)  # Uploaded data
        
            # Extract roll numbers from pre-existing data
            std = set(str(roll_no).lower() for roll_no in df1["Roll No"])
        
            # Extract email prefixes from uploaded data
            substd = set(str(email)[:-14] for email in df2[a])
        
            # Find missing elements
            mis = std - substd
        
            # Create DataFrame from missing elements with student names
            missing_data = [{"Status": "Submitted", "Count": len(std)}, {"Status": "Missing", "Count": len(mis)}]
            mis_df = pd.DataFrame(missing_data)
        
            # Display bar graph comparing lengths of 'mis' and 'std'
            st.bar_chart(mis_df.set_index("Status"))

            # Display DataFrame of missing elements
            st.dataframe(mis_df)

        except Exception as e:
            st.error(f"An error occurred: {e}")
