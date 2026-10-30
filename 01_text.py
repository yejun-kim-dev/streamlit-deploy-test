import streamlit as st

st.title("text elements")
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')
st.header('Header 연습')
st.subheader('Subheader 연습')
st.text('text 연습')
st.caption('caption 연습')


# markdown 연습하기
st.markdown("# This is a Markdwon title") # #제목
st.markdown("## This is a Markdwon title")# ##중제목?
st.markdown("This is **the Markdwon 진하게**")
st.markdown("This is _the Markdwon 기울임_")
st.markdown("This is *the Markdwon 기울임*")
st.markdown("This is **_the Markdwon 진하고 기울임_**")
st.markdown('- item')
st.markdown('1. item')

# Code, LaTex-수학식 표현
st.code('x=1234')
st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)
''')

# write 연습하기
st.write('this is a string write \n')
st.write('\n')
st.write('\n')
st.write("Hello, *World!* :sunglasses:")