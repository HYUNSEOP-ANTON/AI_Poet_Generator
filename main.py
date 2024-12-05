#from dotenv import load_dotenv
#load_dotenv();
#load_dotenv(override=True) 

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

#subject = 'AI';
#result = chat_model.invoke(subject + "에 대한 설명을 100자 이내로 해줘 ");
#print(result.content);

import streamlit as st

st.title("인공지능 시인 powered by OpenAI")
subject = st.text_input("시의 주제를 입력해주세요");
st.write("입력된 시의 주제 : " + subject);

if st.button("시 작성하기"):
    with st.spinner("작성 중..."):
        result = chat_model.invoke(subject + "에 대한 시를 써주겠어요?");
        st.write(result.content);

