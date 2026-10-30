import streamlit as st
import random

st.title(':yellow[점심 메뉴 추천]')

category = st.selectbox('오늘은 어떤 음식이 끌리나요?', ['한식', '중식', '일식', '양식'])
money = st.selectbox('오늘 점심 예산은 얼마인가요?', ['5천원 이하', '1만원 이하', '1만 5천원 이하', '2만원 이하'])
spicy = st.radio('매운음식을 좋아하시나요?', ['네', '아니요'])

food = {
    '한식': ['김치찌개', '비빔밥', '제육볶음'],
    '중식': ['짜장면', '짬뽕', '볶음밥'],
    '일식': ['초밥', '라멘', '우동'],
    '양식': ['파스타', '리조또', '햄버거'],
    '분식': ['떡볶이', '김밥', '라면']
}

if st.button('추천받기'):
    if category in food:
        recommended_food = random.choice(food[category])
        st.write(f'오늘의 추천 메뉴는 :green[{recommended_food}]입니다!')
    else:
        st.write('죄송합니다. 추천할 메뉴가 없습니다.')