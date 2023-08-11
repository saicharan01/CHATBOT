import streamlit as st
import snowflake.connector

def main():
    st.title("Snowflake Connection Setup")

    # Snowflake account details
    account = st.text_input("Snowflake Account URL (without https://):")
    region = st.selectbox("Region:", ["central-india.azure"])
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    database = st.text_input("Database:")

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

