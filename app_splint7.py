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
st.caption('スプリント7の演習です ver 0.93')

code = '''
演習の仕様は以下の通りです。
ユーザーからの口コミのテキスト、画像、メールアドレス、氏名の入力に基づき、受信した口コミは Amazon DynamoDB に保存され、口コミ内容は Amazon Comprehend による感情分析を行い、その結果に基づいてカスタマイズされたお礼メールを、Amazon SES を介してユーザーに自動送信します。
また、画像はプロモーション用として使用するため、不適切な内容が含まれていないか、Amazon Rekognition による事前チェックを行います。(現在工事中)
口コミの投稿は、API Gateway を用いた API として呼び出されます。API のレスポンスを早めるため、API では口コミと画像のアップロードのみを行い、その後の分析やメール送信は、Amazon SQS を介して実行される AWS Step Functions のステートマシーンにより実行されます。

なお、webアプリは、streamlit よりwebアプリを形成し、作成したREST APIをコールする(任意)
streamlit で利用する Python コードは、ローカルPCで開発し、Git Hub に登録することで、streamlit と連携が可能となる。
そのため、ローカル PC での開発にVSCode を用いることで、Git Hub経由で streamlit 上の Pythonコードをアップデートすることが可能となる。
'''
# python言語用のシンタックスハイライトを表示する(コード上)
st.code(code, language='python')

st.text('ただいま、一部工事中であり、指定する画像ファイルの,')
st.markdown(":red[ディレクトリするパスは明記してください]")

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

# video_file = open('unicorn.mid', 'rb')
# video_bytes = video_file.read()
# st.video(video_bytes)

with st.form(key='profile_form'):

#        # テキストボックス
#        name = st.text_input('名前')
#        address =st.text_input('住所')
#        print(name)
#
#        #セレクトボックス
#        age_category = st.selectbox(
#                '年齢層',
#                ('子ども(18歳未満)','大人(18歳以上)'))
#        
#        #ラジオボタン
#        age_category = st.radio(
#                '年齢層',
#                ('子ども(18歳未満)','大人(18歳以上)'))
#        
#        #複数選択
#        hobby = st.multiselect(
#                '趣味',
#                ('スポーツ','読書','プログラミング','アニメ・映画','釣り','料理'))

        # APIコール用引数項目
        reviewText = st.text_input('レビューコメント ⇒ コメント内容によりご挨拶メールの内容が変わります。好意的な度合いにより3種類')
        userName = st.text_input('お名前')
        mailAddress = st.text_input('メールアドレス')
#        uploaddir = st.text_input('下記のアップロードする画像ファイルのディレクトリをフルパスで、記載してください ⇒ 現在は工事中のため特別仕様')
##        imagePath = st.text_input('画像ファイル名 ⇒ 工事中のため「egao.png」または、「ikari.png」をコピペしてください')

# 2024/10/15 start
        # https://qiita.com/kins/items/52a52c2c000e364ab452
#        st.markdown('# 画像を保存するデモ')

#        IMG_PATH = 'imgs'
#        IMG_PATH = 'C:\temp\pythonProject1\streamlit'
        #アップロード用の画像ファイルをローカルPC上にディレクトリとして作成してもらい、そこに画像ファイルを配置してもらう
        PATHDIR = '/temp/images'       
#        PATHDIR = '/temp/pythonProject1/streamlit/imgs'        
        file = st.file_uploader('jpg, jpeg, png形式の画像をアップロードしてください', type=['jpg', 'jpeg', 'png'])
#        st.markdown(f'{file.name} をアップロードしました.')
#        filename = os.path.join(IMG_PATH, file.name)

# 2024/10/15 end

## test start 
        st.markdown('# 画像を保存するデモ')
        file = st.file_uploader('画像をアップロードしてください.', type=['jpg', 'jpeg', 'png'])
        PATHDIR2 = 'imags'  
        if file:
                st.markdown(f'{file.name} をアップロードしました.')
                img_path = os.path.join(PATHDIR2, file.name)
                print("test img_path") 
                print(img_path)
                # 画像を保存する
                with open(img_path, 'wb') as f:
                        f.write(file.read())
                
                # 保存した画像を表示
                img = Image.open(img_path)
                st.image(img)
## test end                

        #ボタン      
        submit_btn = st.form_submit_button('送信')
        cansel_btn = st.form_submit_button('キャンセル')
        
        if submit_btn:
                
# 2024/10/15 start
#                print("uploaddir") 
#                print(uploaddir)
                print("file-1 ") 
                print(file.name)
                print(file)
                
                imagePath = file.name
# 2024/10/15 end
                st.text(f'ようこそ {userName} さん!{mailAddress}にメールを送りました!')
#                st.text(f'年齢層: {age_category}')
#                st.text(f'趣味: {", ".join(hobby)}')

                # ここから
                # 参考　https://qiita.com/inoue-mn/items/44043e68e5d054bb4ed1
#                url = "https://5qoczcx7a7.execute-api.ap-northeast-1.amazonaws.com/dev"
#                headers = {'content-type': 'application/json; charset=UTF-8'}
#                payload = {
#                "reviewText": "すごくいい感じに仕上がっていると思います",
#                "userName": "curlより書き込み次郎",
#                "mailAddress": "xxx@gmail.com",
#                "imagePath":"jinmeister-file-storage-20240912/file_test2.png"
#                }
#
#                res = requests.post(
#                        url,
#                        data=json.dumps(payload), 
#                        headers=headers
#                        )

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
# 2024/10/15 start
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

#                img_path = os.path.join(IMG_PATH, file.name)
## test                img_path = os.path.join(PATHDIR, file.name)
#                IMG_PATH = 'c:/temp/pythonProject1/streamlit/imgs'
#                img_path = os.path.join(file.name)

                img_path = os.path.join(PATHDIR, file.name)
#                img_path = os.path.join(uploaddir, file.name)
#                img_path2 = img_path.replace('/', os.sep)
                # test
#                img_path2 = r'C:\temp\pythonProject1\streamlit\imgs\IMG_2207.PNG'
                # test
                print("img_path") 
                print(img_path)
#                print("img_path2") 
#                print(img_path2)

                # openするファイル(img_path)は、S3バケットに保存されるファイルであり、
                # 実在するローカル環境のディレクトリフルパス + ファイル名 である必要がある。
                ospath = os.getcwd()
                print("ospath")
                print(ospath)


                with open(img_path, 'rb') as file:
#                with open(file.name, 'rb') as file:
                        res = requests.put(url, data=file, headers=headers)

#                res = requests.put(
#                        url,
#                        headers=headers
#                        )
# 2024/10/15 end
                
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