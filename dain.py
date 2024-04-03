import streamlit as st
import pandas as pd

st.title('Tech Quest Data Analyst')

file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])
sub = st.button('Analyse')

if sub:
    if file is not None:
        st.subheader("The results")
        try:
            df1 = pd.read_excel("Csbs.xlsx")  # Pre-existing data
            df2 = pd.read_excel(file)  # Uploaded data

            # Extract roll numbers from pre-existing data
            std = set(str(roll_no) for roll_no in df1["Roll No"])
            date = df2["Timestamp"]
            td = date[0]
            st.write(f"Date : {str(td)[:-16]}")
            # Extract email prefixes from uploaded data
            
            substd = set(str(email)[:-14].upper() for email in df2["Email Address"])
            
            # Find missing elements
            mis = std - substd

            # Create DataFrame from missing elements with student names
            missing_data = [{"Status": "Submitted", "Count": len(substd)}, {"Status": "Missing", "Count": len(mis)}]
            mis_df = pd.DataFrame(missing_data)

            # Display bar graph comparing lengths of 'mis' and 'std'
            st.bar_chart(mis_df.set_index("Status"))
            st.subheader("Non-submitted students")
            # Display DataFrame of missing elements with student names
            date = df2["Timestamp"]
            mi_df = pd.DataFrame({"Roll No": list(mis)})
            mi_df = mi_df.merge(df1[['Roll No', 'Student Name']], on='Roll No', how='left')
            st.dataframe(mi_df)

        except Exception as e:
            st.error(f"An error occurred: {e}")
