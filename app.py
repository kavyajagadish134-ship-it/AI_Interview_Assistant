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
mode = st.radio("Activity",["General Question","Generate Code Questions" , "Evaluate Answers", "Improve Answer"])
if mode =="Generate Question" :
    count = st.slider("Number Of Questions",1,10,5)
elif mode =="Generate code Questions" :
    topic = st.selectbox( "Select Topic",
                         [ "Python", "C++", "C", "DSA", "Aptitude","Java"])
    count= st.slider("Number of Questions",1,10,5)
else:
    question = st.text_area("Enter Interview Question Here")
    answer = st.text_area("Enter Your Answer", height=160)
    if st.button("Generate AI Respons",type="primary"):
        if mode == (["Evaluate Answers","Improve Answer"]and(not question.strip()) or (not answer.strip())):
            st.warning("please enter a valid question and answer")
            st.stop()
        topics == "Topics is" + topic + "Difficulty is" + level
        if mode == "Generate Question":
           task == "Generate" + str(count) + "Frequently asked Interview Questions 3 theory and 2 logical Question. Donot give answers.give hints."
        elif mode  == "Generate Code Questions":
            task == "Generate"+ str(count) + "Frequently asked  coding questions on topicon topic "+topic+"and give hints to slove them.Be accurate."
        elif mode =="Evaluate Answers":
            task == " Question : " +question+ "My Answer :" +amnswer+ "Evaluate Answers."
        elif mode =="Improve Answers"
            task == " Question : " +question+ "My Answer :" +amnswer+ "Improve Answers."
            background =="Job role : "+role+ "Difficulty level" + level
            with st.spinner("Genrating your answer ....."):
              try:
                 response = client.chat.completions.create(
                  model="openai/gpt-oss-120b",
                  messages=[{"role":"system","content":"You are an expert Technical Interviewer"},
                            {
                                "role":"user",
                                "content":"""Generate 5 freqently asked interviewer questions,
                                 concepts are python ,AI,LLMS,
                                 give both questions and answer how to answer"""}
                           ],
                  temperature=0.7,
                  max_tokens=90000)
                ouptput = response.choices[0].message.content
                st.subheader("AI Response")
                st.markdown(output)
                st.downlode_dutton("Download Response",output ,file_name="Interview_Response,txt",mime = 'text/plain')
                )
            except Exception as e:
                st.error("API commection was unsuccessful :",e)
                st.info("Please check your API key and rate limits")
        st.caption("Powered by Streamlit.io and GitHub.Using LLM API")
