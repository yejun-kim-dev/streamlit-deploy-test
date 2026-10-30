import streamlit as st
import random

st.header('오늘의 운세')

name = st.text_input('이름을 입력하세요', key='name')

np = ["오늘은 새로운 도전을 해보기에 좋은 날입니다.",
      "작은 실수가 있어도 너무 걱정하지 마세요.",
      "좋은 아이디어가 떠오를 수 있습니다.",
      "오늘은 휴식이 필요한 날입니다.",
      "주변 사람과의 대화에서 좋은 기회를 얻을 수 있습니다."
]
st.button('운세 보기', key='btn_lucky')
    if button:
        st.write(f"{st.name}님의 오늘의 운세: ")
        st.write(random.choice(np))
    st.write(random.choice(np))