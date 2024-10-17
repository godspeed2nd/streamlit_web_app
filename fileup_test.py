# https://qiita.com/firesign2023/items/2a249dd06a6f4c604c0d
# 起動方法
# streamlit run fileup_test.py & sleep 3 && npx localtunnel --port 8501

import streamlit as st
import pandas as pd
import os

# 画像保存先のディレクトリを設定
IMG_PATH = '/temp/pythonProject1/streamlit/imgs'
#IMG_PATH = '/content/images'

# 画像保存先のディレクトリが存在しない場合は作成
if not os.path.exists(IMG_PATH):
    os.makedirs(IMG_PATH)
    
def list_imgs():
    # IMG_PATH 内の画像ファイルを列挙
    return [
        filename
        for filename in os.listdir(IMG_PATH)
        if filename.split('.')[-1] in ['jpg', 'jpeg', 'png']
    ]

def main():
  st.markdown('# 画像を保存するデモ')
  # IMG_DIR 以下の画像から選択
  filename = st.selectbox('ダウンロードする画像を選択', list_imgs())
  # ダウンロード
  st.download_button(
    'ダウンロード',
    open(os.path.join(IMG_PATH, filename), 'br'),
    filename
  )

  file = st.file_uploader('画像をアップロードしてください.', type=['jpg', 'jpeg', 'png'])
  if file:
    st.markdown(f'{file.name} をアップロードしました.')
    img_path = os.path.join(IMG_PATH, file.name)
    # 画像を保存する
    with open(img_path, 'wb') as f:
      f.write(file.read())
            
    # 保存した画像を表示
    img = Image.open(img_path)
    st.image(img)
