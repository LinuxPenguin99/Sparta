import os
from openai import OpenAI
import streamlit as st

# Not Secret
'''
os.environ['OPENAI_API_KEY'] = ''
client = OpenAI(
    api_key = os.environ.get('OEPNAI_API_KEY'),
    )
'''
# Screte
os.environ['OPEN_API_KEY'] = st.secrets['API_KEY']
client = OpenAI(api_key = os.environ.get('OPENAI_API_KEY'))

def chatgpt(keyword):
    chat_completion = client.chat.completions.create(
        messages = [
            {
                'role': 'user',
                'content': keyword,
                },
            {   'role': 'system',
                'content': '입력 받은 키워드에 대한 흥미진진한 300자 이내의 시나리오를 작성해줘',
                }
            ],
        model = 'gpt-4o',
        )
    result = chat_completion.choices[0].message.content
    return result
        
st.title('Super Scenario Bot 🥸')

keyword = st.text_input('Input Keyword')

if st.button('Generate'):
    st.write(chatgpt(keyword))