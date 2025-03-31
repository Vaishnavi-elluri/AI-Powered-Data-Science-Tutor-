
import streamlit as st
import google.generativeai as genai

# Set API Key securely
GOOGLE_GENAI_API_KEY = "AIzaSyDxq34Z3EtWUEA8uSfgOAigJgwOAQQ0yCc"
genai.configure(api_key=GOOGLE_GENAI_API_KEY)

# Function to get AI response
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro",system_instruction=
                                      """You are helpful AI tutor for Data Science.
                                      You are expected to reply as much as in detail. In case
                                      if the query is not related to Data Science politely decline 
                                       and tell them to ask the question in Data Science domain only""")  # Ensure correct model name
        response = model.generate_content(prompt) 
        return response.text if hasattr(response, "text") else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("AI-Powered Data Science Tutor 🤖")

# User input
user_input = st.text_area( "Ask me any Data Science-related question")


if st.button("Submit") and user_input:
    with st.spinner("Processing your query... ⏳"):
        response = get_gemini_response(user_input)
    st.success("Here's your answer!")
    st.subheader("AI's Response:")
    st.write(response)
    st.markdown(response)
    
