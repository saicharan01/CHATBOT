import streamlit as st
import snowflake.connector
import time

def main():
    st.title("Snowflake Manual Connection")

    # Snowflake account details
    account = "xc60341.central-india.azure.snowflakecomputing.com"
    region = "central-india" 
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

            # Execute a simple query
            cursor = conn.cursor()
            cursor.execute("SELECT CURRENT_VERSION()")
            result = cursor.fetchone()

            # Display the query result
            st.write("Connected to Snowflake!")
            st.write("Snowflake Version:", result[0])

            # Close the cursor and connection
            cursor.close()
            conn.close()
        except snowflake.connector.errors.DatabaseError as e:
            st.error(f"Connection failed. Error: {e}")

if __name__ == "__main__":
    main()
