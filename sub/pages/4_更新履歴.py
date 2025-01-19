import streamlit as st
import pandas as pd

st.title('Cloud Tech Academy')
st.caption('スプリント7の演習です ver 1.0')

# 以下の記述は効果出ていない謎
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

# 以下の記述は効果出ていない謎

#以下のディレクトリがローカルPCのどこに該当するのか不明・・・
#ディレクトリが画像もないのに表示される。。。謎
#image = '/app/static/image.png'
#image = 'c:/temp/pythonProject1/streamlit/CloudTech_Splint7/sub/static/image_a.png'
image = '/static/image_a.png'
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
    <p class='my-text'>更新履歴<br>
    """, unsafe_allow_html=True)

df = pd.DataFrame({
    'バージョン': ['0.5','0.95','1.0','1.5'],
    '更新日': ['2024/10/15','2024/10/18','2024/10/18','2025/01/19'],
    '内容': ['αリリース','βリリース','Streamlitサイトサービス開始(ミラーサイト : https://appwebapp-tatb6fzbsodmepomxxyzjo.streamlit.app/)','EC2環境にてサービス開放(http://ec2-54-249-108-169.ap-northeast-1.compute.amazonaws.com:8501/)'],
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


