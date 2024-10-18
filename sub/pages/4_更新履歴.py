import streamlit as st
import pandas as pd

st.title('Cloud Tech Academy')
st.caption('スプリント7の演習です ver 1.1')

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://claris20230923.s3.ap-northeast-1.amazonaws.com/cloudtechacademy_logo.png");
    }
   </style>
    """,
    unsafe_allow_html=True
)

image = 'cloudtechacademy_logo.png'
css = f'''
<style>
    .stApp {{
        background-image: url({image});
        background-size: cover;
        background-position: center;
        background-color:rgba(255,255,255,0.4);
    }}
    .stApp > header {{
        background-color: transparent;
    }}
</style>
'''
st.markdown(css, unsafe_allow_html=True)

# HTML埋め込み
st.markdown("""
    <style>
    .my-text {
        color: white;
        font-size: 24px;
        background-color: #008080;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    <p class='my-text'>更新履歴</p>
    """, unsafe_allow_html=True)

df = pd.DataFrame({
    'バージョン': ['0.5','1.1'],
    '更新日': ['2024/10/15','2024/10/18'],
    '内容': ['αリリース','正式リリース'],
})

primaryColor = "#0000FF"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F0F0"
textColor = "#000000"

# 表示
st.write(df)

# st.dataframe(df, width=200, height=240)
# 表示
# st.write(df)


