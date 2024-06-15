import streamlit as st
import os
from openai import OpenAI
import json

st.set_page_config(layout="wide")

file_path = './face_data.json'

with open(file_path, 'r') as file:
    data = json.load(file)

os.environ["OPENAI_API_KEY"] = st.secrets["API_KEY"]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

emotion = data["dominant_emotion"]
age = data["age"]
gender = data["dominant_gender"]
gender_t = str
if gender == 'Man':
      gender_t = '남성'
elif gender == 'Woman':
      gender_t = '여성'
emotion_t = str
if emotion == 'happy':
      emotion_t = '행복'
original_title = '<p color:Blue; font-size: 60px;">큰일 낼 수 있는 당신을 위한 큐레이션</p>'
st.markdown('# :red[큰일 낼 수 있는 당신]을 위한 큐레이션', unsafe_allow_html=True)
st.write("  ")
st.write("  ")

col1, col2 = st.columns([1, 3], gap="medium")

with col1:
  response = client.images.generate(
    model="dall-e-3",
    prompt="기분 좋게 하는 캐릭터 이미지 생성해줘. 솔직히 네가 만드는 이미지 너무 다 중국스러워. 중국스럽지 않은 3D 캐릭터를 생성해줘.",
    size="1024x1024",
    quality="standard",
    n=1,
  )
  image_url = response.data[0].url
  st.image(image_url)

with col2:
  st.markdown(f'# {age}세, {gender_t}인 당신\n # 오늘의 기분은 {emotion_t}하시군요')
  st.write("  ")
  on = st.toggle("따뜻하게 말해주면 좋겠어요.")


if on:
    prompt = '나는 mbti 세 번째 글자가 F야. 나는 아주 감성적인 사람이야. 그러니까 공감 100% 말투로 대답해줘'
else:
    prompt = '나는 mbti 세 번째 글자가 T야. 나는 아주 이성적인 사람이야. 그러니 공감하는 말투는 꿈도 꾸지마. 아주 냉철한 판단으로 대답해주길 바라.'

with st.spinner('생성 중입니다.'):
  chat_completion1 = client.chat.completions.create(
      messages=[
        {"role": "system", "content": "너는 매일 아침 나에게 그날의 명언을 알려주는 큐레이터야. 오늘 나의 조건에 맞는 명언을 300자 이내로 줘." + prompt},
        {"role": "user", "content": f"1. 감정 : ${emotion}\n2. 나이 : ${age}\n3. 성별 : ${gender}\n"},
      ],
    model="gpt-4o",
  )
  chat_completion2 = client.chat.completions.create(
      messages=[
        {"role": "system", "content": "너는 매일 아침 나에게 그날의 운세을 알려주는 큐레이터야. 오늘 나의 조건에 맞는 운세를 300자 이내로 줘." + prompt},
        {"role": "user", "content": f"1. 감정 : ${emotion}\n2. 나이 : ${age}\n3. 성별 : ${gender}\n"},
      ],
    model="gpt-4o",
  )
  chat_completion3 = client.chat.completions.create(
      messages=[
        {"role": "system", "content": "너는 매일 아침 나에게 그날의 잡학상식을 알려주는 큐레이터야. 오늘 나의 조건에 맞는 잡학상식을 300자 이내로 줘." + prompt},
        {"role": "user", "content": f"1. 감정 : ${emotion}\n2. 나이 : ${age}\n3. 성별 : ${gender}\n"},
      ],
    model="gpt-4o",
  )


  result1 = chat_completion1.choices[0].message.content
  result2 = chat_completion2.choices[0].message.content
  result3 = chat_completion3.choices[0].message.content
  
  col1, col2, col3 = st.columns(3)

  with col2:
    st.header("오늘 하루는 이럴 것 같아요..")
    with st.container(height=350):
      st.write(result1)

  with col1:
    st.header("이런 말씀을 해드리고 싶어요..")
    with st.container(height=350):
      st.write(result2)

  with col3:
    st.header("오늘은 이런 지식을 알아볼까요?")
    with st.container(height=350):
      st.write(result3)