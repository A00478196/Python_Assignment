
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



def main():
    st.title("Simple Streamlit App")


    # Add a file uploader
    uploaded_file = st.file_uploader("Choose a file", type=["csv"])
    if uploaded_file is not None:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)

        if len(df.columns) != 2:
            st.error("Error: The uploaded CSV file must have exactly 2 columns.")
        else:
            # Display the DataFrame
            st.write("Uploaded CSV file:")
            st.write(df)
            st.header("Age Histogram")
            plt.hist(df["Age"], bins=20, color='lightpink')
            st.set_option('deprecation.showPyplotGlobalUse', False)

            plt.xlabel("Age")
            plt.ylabel("Count")
          
            st.pyplot()




if __name__ == "__main__":
    main()
