# ローカル環境での起動方法
#        PS C:\temp\pythonProject1\streamlit\CloudTech_Splint7> streamlit run app_splint7.py

# https://www.youtube.com/watch?v=4nsTce1Oce8&t=1696s

import streamlit as st
from PIL import Image
import requests
import json
import os


st.title('Cloud Tech Academy')
st.caption('スプリント7の演習です ver 1.0')

st.subheader('演習紹介')

code = '''
Cloud Tech の紹介を以下より参照し、レビューコメントをください。
https://kws-cloud-tech.com/#
'''

# python言語用のシンタックスハイライトを表示する(コード上)
st.code(code, language='python')

with st.form(key='profile_form'):
        # APIコール用引数項目
        reviewText = st.text_input('レビューコメント ⇒ コメント内容によりご挨拶メールの内容が変わります。好意的な度合いにより3種類[必須]')
        userName = st.text_input('お名前[必須]')
        mailAddress = st.text_input('メールアドレス[必須]')

        #アップロード用の画像ファイルをローカルPC上にディレクトリとして作成してもらい、そこに画像ファイルを配置してもらう
#        PATHDIR = '/temp/images'       
        PATHDIR = ''       

#        file = st.file_uploader('jpg, jpeg, png形式の画像をアップロードしてください ⇒ 画像ファイルは予め /temp/images/画像ファイル.png に配置しておいてください。', type=['jpg', 'jpeg', 'png'])
        file = st.file_uploader('jpg, jpeg, png形式の画像をアップロードしてください[任意]', type=['jpg', 'jpeg', 'png'])
#       PATHDIRのディレクトリは事前に必要。だが、ファイルはどこのディレクトリから指定してもよい。

        #ボタン      
        submit_btn = st.form_submit_button('送信')
        cansel_btn = st.form_submit_button('キャンセル')

        if submit_btn:
                
                if file is None:
                        imagePath = ""
                else:
                        imagePath = file.name

                print("imagePath") 
                print(imagePath)

                st.text(f'ようこそ {userName} さん!{mailAddress}にメールを送りました!')

                url = "https://5qoczcx7a7.execute-api.ap-northeast-1.amazonaws.com/dev"
                headers = {'content-type': 'application/json; charset=UTF-8'}
                payload = {
                "reviewText": reviewText,
                "userName": userName,
                "mailAddress": mailAddress,
                "imagePath": imagePath
                }

                res = requests.post(
                        url,
                        data=json.dumps(payload), 
                        headers=headers
                        )
                # ここまで

                print(res.status_code) # 応答のHTTPステータスコード
                print(res.text) # 応答のテキスト表示
                print(res.json()) # 応答のJSON表示
                st.text(f'応答のJSON表示: {res.json()}')

                url1 = "https://5qoczcx7a7.execute-api.ap-northeast-1.amazonaws.com/dev/fileupload-test-baket-20240911/"

                if file is None:
                        url2 = ""
                else:
                        url2 = file.name
                        
                url = url1 + url2

                print("url") 
                print(url)

#                print("file-2") 
#                print(file.name)
                
                headers = {
                        "Content-Type": "image/png"
                }

#                img_path = os.path.join(PATHDIR, file.name)

#                print("img_path") 
#                print(img_path)

                # openするファイル(img_path)は、S3バケットに保存されるファイルであり、
                # 実在するローカル環境のディレクトリフルパス + ファイル名 である必要がある。
                ospath = os.getcwd()
                print("ospath")
                print(ospath)

                res = requests.put(url, data=file, headers=headers)

                print(res.status_code) # 応答のHTTPステータスコード
                print(res.text) # 応答のテキスト表示
#                print(res.json()) # 応答のJSON表示
                st.text(f'画像upのHTTPステータスコード: {res.status_code}')
                
#                with open(img_path, 'rb') as file:
#                with open(file.name, 'rb') as file:
#                        res = requests.put(url, data=file, headers=headers)

                
