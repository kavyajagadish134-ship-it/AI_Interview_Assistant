import streamlit as st
from groq import Groq

st.set_page_config(page_title='LLM', layout='centered')

st.title('AI Interview')
st.caption('Practice and Prepare for your placement')

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

except (KeyError, FileNotFoundError):
    st.error("API key is missing. Add it in Advanced Settings.")
    st.stop()
role = st.selectbox("Job Title", ["Machine Learning Engineer", "Senior Software Engineering", "Full Stack Engineer", "Backend Engineer", "Others"])

if role =="Others":
    st.text_input("Enter your Job Title","XXXXXX")
model = st.selectbox(
    "Choose Your Model",
    [
        "openai/gpt-oss-120b",
        "openai/gpt-oss-20b"
    ]
)
level=st.selectbox(
    "Choose your level",
    [
        "Beginner", "Intermediate", "Advanced"
    ]
)
mode = st.radio("Activity",["General Question", "Generate Code Questions", "Evaluate Answers", "Improve Answer"])
if mode =="Generate Question" :
    count = st.slider("Number Of Questions",1,10,5)
elif mode =="Generate code Questions" :
    topic = st.selectbox( "Select Topic",
                         [ "Python", "C++", "C", "DSA", "Aptitude","Java"])
    count= st.slider("Number of Questions",1,10,5)
else:
    question = st.text_area("Enter Interview Question Here")
    answer = st.text_area("Enter Your Answer", height=160)
