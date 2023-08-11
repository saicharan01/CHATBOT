import streamlit as st
import pandas as pd
import requests
import snowflake.connector

def main():
    st.title("Snowflake Information Collector")
    
    # Collect user input
    account = st.text_input("Snowflake Account URL (without https://):")
    region = st.selectbox("Region:", ["us-east-1", "us-west-2", "eu-west-1"])  # Add more regions if needed
    database = st.text_input("Database:")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    
    if st.button("Collect Info"):
        # Connect to Snowflake
        conn = snowflake.connector.connect(
            user=username,
            password=password,
            account=account,
            region=region,
            database=database
        )
        
        st.write("Connected to Snowflake!")
        st.write("Collected Information:")
        st.write(f"Snowflake Account: {account}")
        st.write(f"Region: {region}")
        st.write(f"Database: {database}")
        
        # Don't forget to close the connection when done
        conn.close()
        
if __name__ == "__main__":
    main()
