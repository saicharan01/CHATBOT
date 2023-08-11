import streamlit as st
import snowflake.connector
import time

def main():
    st.title("Snowflake Manual Connection")

    # Snowflake account details
    account = "xc60341.central-india.azure.snowflakecomputing.com"
    region = "central-india.azure"  # Use the correct region code
    username = "SAICHARAN11"
    password = "Saicharan@1101"
    database = "MY_DB"

    if st.button("Connect"):
        conn_params = {
            "user": username,
            "password": password,
            "account": account,
            "region": region,
            "database": database
        }

        try:
            # Establish a connection
            conn = snowflake.connector.connect(**conn_params)

            # Execute a simple query to verify connection
            cursor = conn.cursor()
            cursor.execute("SELECT CURRENT_REGION(), CURRENT_ACCOUNT(), CURRENT_DATABASE(), CURRENT_USER()")
            result = cursor.fetchone()

            # Display the query result
            st.write("Connected to Snowflake!")
            st.write("Current Region:", result[0])
            st.write("Current Account:", result[1])
            st.write("Current Database:", result[2])
            st.write("Current User:", result[3])

            # Close the cursor and connection
            cursor.close()
            conn.close()
        except snowflake.connector.errors.DatabaseError as e:
            st.error(f"Connection failed. Error: {e}")

if __name__ == "__main__":
    main()
