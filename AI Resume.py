import streamlit as st

import google.genai as genai

google_api_key = st.secrets["google"]["api_key"]

client = genai.Client(api_key = google_api_key)

model = genai.Genai('gemini-2.5-flash')

# genai.configure(api_key=google_api_key)

# model = genai.GenerativeModel('gemini-2.5-flash')


#1. AI Cover Letter Generator
#- Create a Streamlit app that:
#- Takes job title and resume summary as input
#- Uses google-generativeai gemini-pro model
#- Prompts Gemini: &quot;Write a cover letter for [job_title] using these resume points:
#[summary]&quot;
#- Displays the output below a submit button

st.title('AI Cover Gnerator')

Job_title = st.text_input("Enter Job Title:")

summary= st.text_input("Enter Resume Summary:")

if st.button("Generate Cover Letter"):
    prompt = f"Write a cover letter for {Job_title} using these resume points: {summary}"
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        content = prompt)
    st.write(response.text)
