import streamlit as st
import pandas as pd


def main_page():
    st.title(':rainbow[main page]')
    st.sidebar.subheader('main🏠')
    #2 Columns
    st.subheader('SNS')
    col1, col2, col3 = st.columns(3)

    # 각 column에 개별 요소 배치
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image('data/picture1.jpeg')
        st.link_button('인스타그램', 'https://www.instagram.com/chico_katzen?dlrf=MnB5YnhxdnUydDB3&utm_source=qr')
    with col2:
        st.image('data/picture2.jpeg')
        st.link_button('블로그', 'https://blog.naver.com/chico_100com')
    with col3:
        st.image('data/picture3.jpeg')
        st.link_button('노션', 'https://app.notion.com/p/sk-Family-AI-6fd2147b11e483aab42201f468dc1485?source=copy_link')


def photo_page():
    st.title(':violet[Photo page]')
    st.sidebar.subheader('photo📷')
    st.text('[배경화면용 이미지]')
    tab1, tab2, tab3 = st.tabs(['no.1', 'no.2', 'no.3'])
    with tab1:
        st.image('data/back_1.png')
    with tab2:
        st.image('data/back_2.jpg')
    with tab3:
        st.image('data/back_3.jpeg')

    st.text('[디카 백업 영상]')
    st.video('data/video1.mp4')

def daily_page():
    st.title(':yellow[Daily page]')
    st.sidebar.subheader('diary📒')
    st.text('[학습 노트]')
    df = pd.read_csv('data/note.csv', encoding='utf-8-sig')
    df_line = df.dropna()                      # 빈칸이 하나라도 있는 행 삭제
    # df_line = df.dropna(subset=['날짜'])      # '날짜' 열이 빈 행만 삭제
    # df_line = df.dropna(how='all')            # 모든 칸이 빈 행만 삭제
    st.dataframe(df_line)
    st.markdown(':yellow-background[**체크리스트**]')  # 굵게 + 노란 배경
    tasks = ['비타민 챙겨 먹기', '노션 기록하기', '블로그 기록하기']
    for task in tasks:
        st.checkbox(task, key=task)
    daily1 = st.text_area("하루 한 문장 : 일기 작성하기")
    st.write("daily: " + daily1)

page_names_to_funcs= {'Main Page': main_page, 'Photo Page': photo_page, 'Daily Page': daily_page}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()





