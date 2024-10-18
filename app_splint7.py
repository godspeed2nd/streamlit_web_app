# ローカル環境での起動方法
#        PS C:\temp\pythonProject1\streamlit\CloudTech_Splint7> streamlit run app_splint7.py

# https://www.youtube.com/watch?v=4nsTce1Oce8&t=1696s


import streamlit as st
from PIL import Image

import requests
import json

import streamlit as st
import pandas as pd
import os

st.title('Cloud Tech Academy')
st.caption('スプリント7の演習です ver 0.941')

code = '''
演習の仕様は以下の通りです。
ユーザーからの口コミのテキスト、画像、メールアドレス、氏名の入力に基づき、受信した口コミは Amazon DynamoDB に保存され、口コミ内容は Amazon Comprehend による感情分析を行い、その結果に基づいてカスタマイズされたお礼メールを、Amazon SES を介してユーザーに自動送信します。
また、画像はプロモーション用として使用するため、不適切な内容が含まれていないか、Amazon Rekognition による事前チェックを行います。(現在工事中)
口コミの投稿は、API Gateway を用いた API として呼び出されます。API のレスポンスを早めるため、API では口コミと画像のアップロードのみを行い、その後の分析やメール送信は、Amazon SQS を介して実行される AWS Step Functions のステートマシーンにより実行されます。

なお、webアプリは、streamlit よりwebアプリを形成し、作成したREST APIをコールする(任意)
streamlit で利用する Python コードは、ローカルPCで開発し、Git Hub に登録することで、streamlit と連携が可能となる。
そのため、ローカル PC での開発にVSCode を用いることで、Git Hub経由で streamlit 上の Pythonコードをアップデートすることが可能となる。

参考
https://streamlit.io/
'''
# python言語用のシンタックスハイライトを表示する(コード上)
st.code(code, language='python')

#st.text('ただいま、一部工事中であり、指定する画像ファイルの')
#st.markdown(":red[アップロードでエラーとなります]")
#st.text('ですが、画像処理以外は動作します。')

st.subheader('自己紹介')
st.text('はじめまして。ごすです。自己紹介としては・・・バイクが好きです\n'
        'よろしくです')

code = '''
Cloud Tech の紹介を以下より参照し、レビューコメントをください。
https://kws-cloud-tech.com/#
'''

# python言語用のシンタックスハイライトを表示する(コード上)
st.code(code, language='python')

image = Image.open('cloudtechacademy_logo.png')
st.image(image, width=200)

with st.form(key='profile_form'):
        # APIコール用引数項目
        reviewText = st.text_input('レビューコメント ⇒ コメント内容によりご挨拶メールの内容が変わります。好意的な度合いにより3種類')
        userName = st.text_input('お名前')
        mailAddress = st.text_input('メールアドレス')

        #アップロード用の画像ファイルをローカルPC上にディレクトリとして作成してもらい、そこに画像ファイルを配置してもらう
        PATHDIR = '/temp/images'       

        file = st.file_uploader('jpg, jpeg, png形式の画像をアップロードしてください ⇒ 画像ファイルは予め /temp/images/画像ファイル.png に配置しておいてください。', type=['jpg', 'jpeg', 'png'])

        #ボタン      
        submit_btn = st.form_submit_button('送信')
        cansel_btn = st.form_submit_button('キャンセル')

        if submit_btn:
                
                print("file-1 ") 
                print(file.name)
                print(file)
                
                imagePath = file.name
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
                url2 = file.name
                url = url1 + url2

                print("url") 
                print(url)

                print("file-2") 
                print(file.name)
                
                headers = {
                        "Content-Type": "image/png"
                }

                img_path = os.path.join(PATHDIR, file.name)

                print("img_path") 
                print(img_path)

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

                
# HTML埋め込み(現在、機能しておらず)
# https://qiita.com/sypn/items/76928609348b5f13b2f5
# https://qiita.com/sypn/items/76928609348b5f13b2f5
st.markdown("""
        <!DOCTYPE html>
        <html>
        <head>
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-GHGRERY4LV"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-GHGRERY4LV');
        </script>
        </head>
        </html>
    """, unsafe_allow_html=True)     