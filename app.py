import streamlit as st

st.title('반갑습니다!')

st.write(':yellow[music] is :orange-background[world of best] :sunglasses:')
# 예제 2
st.write(   "2026.10.21")

if st.button('노크하기'):
    st.write('여기 사람 있어요 히히')

st.write("정보 수집에 동의하시면 아래 내용에 체크해 주세요")
agree = st.checkbox("동의합니다.")
if agree:
    st.write("이얏호!")

option = st.selectbox(
"가장 즐기는 취미는?",
("음악감상", "영화관람", "독서", "게임", "운동"))
st.write("선택한 방식:", option)

like = st.slider("당신은 음악을 얼마나 좋아하나요?", 0, 100, 50)
st.write("당신은 음악을 ", like, "% 만큼 좋아합니다!")

text1 = st.text_input("이름을 입력하세요.")
text2 = st.text_area("자기소개 해주세요.")
st.write("이름 입력값: " + text1)
st.write("자기소개 입력값: " + text2)

col1, col2 = st.columns(2) # 두 개의 컬럼 생성. 표현하고 싶은
#내용을 열 데이터로 나눠 보여주고 싶을 떄 사용합니다.
with col1:
    text1 = st.text_input("음악감상을 즐기는 이유가 뭔가요?")
with col2:
    text2 = st.text_area("음악감상을 즐기지 않는 이유가 뭔가요?")
st.write("1번 입력값: " + text1)
st.write("2번 입력값: " + text2)

with col2:
    with st.form("form을 사용합니다"):
        text3 = st.text_input("음악감상에 대한 의견을 입력해주세요.")
        text4 = st.text_area("음악감상에 대한 의견을 입력해주세요.")
        submitted = st.form_submit_button("제출")
    if submitted:
        st.write("1번 입력값: " + text3)
        st.write("2번 입력값: " + text4)
    else:
        st.write("1번 입력값: ")
        st.write("2번 입력값: ")