import streamlit as st
import snowflake.connector
import time

def main():
    st.title("Snowflake Information Collector")
    
    # Collect user input
    account = st.text_input("Snowflake Account URL (without https://):")
    region = st.selectbox("Region:", ["us-east-1", "us-west-2", "eu-west-1","Central India (Pune)"])  # Add more regions if needed
    database = st.text_input("Database:")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    
    if st.button("Collect Info"):
        max_retries = 3
        retry_delay = 5  # in seconds
        
        for attempt in range(1, max_retries + 1):
            try:
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
                break  # Successful connection, exit loop
            except snowflake.connector.errors.DatabaseError as e:
                st.write(f"Connection attempt {attempt} failed. Retrying...")
                time.sleep(retry_delay)
        else:
            st.error("Failed to connect after multiple attempts. Please check your credentials and network.")

if __name__ == "__main__":
    main()
