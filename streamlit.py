import streamlit as st

def main():
    st.title("Snowflake Information Collector")
    
    # Collect user input
    account = st.text_input("Snowflake Account URL (without https://):")
    region = st.selectbox("Region:", ["us-east-1", "us-west-2", "eu-west-1"])  # Add more regions if needed
    database = st.text_input("Database:")
    
    if st.button("Collect Info"):
        st.write("Collected Information:")
        st.write(f"Snowflake Account: {account}")
        st.write(f"Region: {region}")
        st.write(f"Database: {database}")
        
if __name__ == "__main__":
    main()

