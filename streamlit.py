import streamlit as st
import openai
import snowflake.connector

# Set your OpenAI API key
openai.api_key = "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"

def main():
    st.title("Snowflake Manual Connection and Chat")

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
            # Establish a connection to Snowflake
            conn = snowflake.connector.connect(**conn_params)

            # Execute a simple query
            cursor = conn.cursor()
            cursor.execute("SELECT CURRENT_VERSION()")
            result = cursor.fetchone()

            # Display Snowflake query result
            st.write("Connected to Snowflake!")
            st.write("Snowflake Version:", result[0])

            # Close Snowflake cursor and connection
            cursor.close()
            conn.close()

        except snowflake.connector.errors.DatabaseError as e:
            st.error(f"Connection failed. Error: {e}")

    # Language model interaction
    st.header("Language Model Interaction")
    prompt = st.text_area("Enter your prompt:")
    if st.button("Generate Response"):
        try:
            # Call the language model to generate a response
            response = openai.Completion.create(
                engine="davinci-codex",  # Choose an appropriate engine
                prompt=prompt,
                max_tokens=50  # Adjust as needed
            )

            # Display the generated response
            st.write("Generated Response:")
            st.write(response.choices[0].text)
        except Exception as e:
            st.error(f"Error generating response: {e}")

if __name__ == "__main__":
    main()
