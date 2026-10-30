import streamlit as st

st.title(':green[MBTI 테스트]')

import streamlit as st

# 선택지 목록 따로 저장
weekend_opts = ['집에서 쉬는 편이다', '밖으로 나가는 편이다']
plan_opts = ['즉흥적으로 움직인다', '계획을 세운다']
study_opts = ['혼자 공부한다', '같이 공부한다']
people_opts = ['낯을 가린다', '금방 친해진다']

# 선택한 값 저장
weekend = st.radio('1. 주말에는 보통?', weekend_opts, key='weekend')
plan = st.radio('2. 여행 갈 때는?', plan_opts, key='plan')
study = st.radio('3. 공부할 때는?', study_opts, key='study')
new_people = st.radio('4. 새로운 사람을 만나면?', people_opts, key='new_people')

if st.button(':red[결과 보기]'):
    if weekend == weekend_opts[0] and plan == plan_opts[0] and study == study_opts[0] and new_people == people_opts[0]:
        st.write(':blue[당신은 감성적인 자유형 입니다.]')
    elif weekend == weekend_opts[1] and plan == plan_opts[1] and study == study_opts[1] and new_people == people_opts[1]:
        st.write(':blue[당신은 활동적인 계획형 입니다.]')
    elif weekend == weekend_opts[0] and plan == plan_opts[1] and study == study_opts[0] and new_people == people_opts[1]:
        st.write(':blue[당신은 차분한 전략형 입니다.]')
    elif weekend == weekend_opts[1] and plan == plan_opts[0] and study == study_opts[1] and new_people == people_opts[0]:
        st.write(':blue[당신은 에너지 넘치는 자유형 입니다.]')
    else:
        st.write(':blue[아직 분류되지 않았습니다.]')
