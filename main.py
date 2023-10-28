import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from pandasai import SmartDataframe

# Create a Streamlit app with a file uploader and a text input box for user queries.
def main():
    st.title("CSV Data Analysis")
    uploaded_file = st.file_uploader("Choose a CSV file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = SmartDataframe(df)

        # Define a function to process user queries and return the appropriate response.
        def process_query(query):
            if "summary" in query.lower():
                return df.describe().to_html()
            elif "plot" in query.lower():
                return "Please enter the column names to plot (comma-separated)"
            else:
                return "Sorry, I don't understand that query."

        # Define a function to plot the data based on user input.
        def plot_data(cols):
            if len(cols) == 2:
                plt.plot(df[cols[0]], df[cols[1]])
                st.pyplot()
            else:
                st.write("Please enter two column names separated by a comma.")

        # Add the necessary Streamlit components to display the response and the plot.
        query = st.text_input("Ask a question about the data")
        df.chat('Which are the countries with GDP greater than 3000000000000?')

if __name__ == "__main__":
    main()
