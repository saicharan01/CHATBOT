import streamlit as st
import openai
import snowflake.connector

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
            conn = snowflake.connector.connect(**conn_params)
            cursor = conn.cursor()
            cursor.execute("SELECT CURRENT_VERSION()")
            result = cursor.fetchone()
            st.write("Connected to Snowflake!")
            st.write("Snowflake Version:", result[0])

            # Close Snowflake cursor and connection
            cursor.close()
            conn.close()

        except snowflake.connector.errors.DatabaseError as e:
            st.error(f"Connection failed. Error: {e}")

    st.header("LLM")
    prompt = st.text_area("Enter your prompt:")
    if st.button("Generate Response"):
        try:
            response = openai.Completion.create(
                engine="davinci-codex",
                prompt=prompt,
                max_tokens=50 
            )

            # Display the generated response
            st.write("Generated Response:")
            st.write(response.choices[0].text)
        except Exception as e:
            st.error(f"Error generating response: {e}")

if __name__ == "__main__":
    main()
