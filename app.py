import streamlit as st
from groq import Groq
st.set_page_config(page_title='LLM', layout='centered')
st.title('AI Interview')
st.caption('Practice and Prepare for your placement')
st.markdown("Launched by BHAVANA J")
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFoundError):
    st.error("API key is missing. Add it in Advanced Settings.")
    st.stop()
role = st.selectbox("Job Title", ["Machine Learning Engineer", "Senior Software Engineering", "Full Stack Engineer", "Backend Engineer", "Others"])
if role == "Others":
    role = st.text_input("Enter your Job Title", "XXXXXX")
model = st.selectbox(
    "Choose Your Model",
    [
        "openai/gpt-oss-120b",
        "openai/gpt-oss-20b"
    ]
)
level = st.selectbox(
    "Choose your level",
    [
        "Beginner", "Intermediate", "Advanced"
    ]
)
mode = st.radio("Activity", ["Generate Question", "Generate Code Questions", "Evaluate Answers", "Improve Answer"])
if mode == "Generate Question":
    count = st.slider("Number Of Questions", 1, 10, 5)
elif mode == "Generate Code Questions":
    topic = st.selectbox("Select Topic", ["Python", "C++", "C", "DSA", "Aptitude", "Java"])
    count = st.slider("Number of Questions", 1, 10, 5)
else:
    question = st.text_area("Enter Interview Question Here")
    answer = st.text_area("Enter Your Answer", height=160)
if st.button("Generate AI Response", type="primary"):
    if mode in ["Evaluate Answers", "Improve Answer"] and (not question.strip() or not answer.strip()):
        st.warning("Please enter a valid question and answer.")
        st.stop()
    if mode == "Generate Question":
        task = "Generate " + str(count) + " Frequently asked Interview Questions: 3 theory and 2 scenario questions. Do not give answers."
    elif mode == "Generate Code Questions":
        task = "Generate " + str(count) + " Frequently asked coding questions on topic " + topic + " and give hints to solve them. Be accurate."
    elif mode == "Evaluate Answers":
        task = "Question:" + question + " My Answer:" + answer + " Evaluate my answer based on correctness, relevance, clarity, completeness. Give a score out of 10 and identify mistakes."
    elif mode == "Improve Answer":
        task = "Question:" + question + " My Answer:" + answer + " Evaluate my original answer, correct technical mistakes, add missing information, provide a complete improved interview answer in natural English."
    background = "Job role: " + role + " Difficulty level: " + level
    with st.spinner("Generating your Answer......"):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": "Act as a senior Interviewer, both HR and Technical expert"
                    },
                    {
                        "role": "user",
                        "content": background + task
                    }
                ],
                temperature=0.7,
                max_tokens=1800
            )
            output = response.choices[0].message.content
            st.subheader("AI Response")
            st.markdown(output)
            st.download_button(
                "Download Response",
                output,
                file_name="Interview_Response.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"API connection was unsuccessful: {e}")
            st.info("Please check your API key and rate limits.")
    st.caption("Powered by Streamlit.io And GitHub")
