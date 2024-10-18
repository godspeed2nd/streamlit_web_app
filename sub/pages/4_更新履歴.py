import streamlit as st
import numpy as np
import pandas as pd

st.title('Cloud Tech Academy')
st.caption('スプリント7の演習です ver 0.95')

df = pd.DataFrame({
    'バージョン': ['0.5','0.95'],
    '更新日': ['2024/10/15','2024/10/18'],
    '内容': ['αリリース','βリリース'],
})

# 表示
st.write(df)