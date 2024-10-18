import streamlit as st
import numpy as np
import pandas as pd

st.title('Cloud Tech Academy')
st.caption('スプリント7の演習です ver 1.0')

df = pd.DataFrame({
    'バージョン': ['0.5','1.0'],
    '更新日': ['2024/10/15','2024/10/18'],
    '内容': ['αリリース','正式リリース'],
})

# 表示
st.write(df)