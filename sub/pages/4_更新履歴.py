import streamlit as st
import numpy as np
import pandas as pd

st.title('Cloud Tech Academy')
st.caption('スプリント7の演習です ver 0.95')

df = pd.DataFrame({
    'バージョン': ['0.95', 2, 3, 4],
    '更新日': ['2024/10/18', 2, 3, 4],
    '内容': ['ベータリリース', 20, 30, 40],
})

# 表示
st.write(df)