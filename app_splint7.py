# https://www.youtube.com/watch?v=4nsTce1Oce8&t=1696s

# 実行方法
# PS C:\temp\pythonProject1\streamlit> streamlit run app.py    

import streamlit as st
from PIL import Image

import requests
import json

import streamlit as st

st.title('Cloud Tech Academy')
st.caption('スプリント7の演習です')

code = '''
演習の仕様は以下の通りです。
ユーザーからの口コミのテキスト、画像、メールアドレス、氏名の入力に基づき、受信した口コミはAmazon DynamoDBに保存され、口コミ内容はAmazon Comprehendによる感情分析を行い、その結果に基づいてカスタマイズされたお礼メールを、Amazon SESを介してユーザーに自動送信します。
また、画像はプロモーション用として使用するため、不適切な内容が含まれていないか、Amazon Rekognitionによる事前チェックを行います。(現在工事中)
口コミの投稿は、API Gatewayを用いたAPIとして呼び出されます。APIのレスポンスを早めるため、APIでは口コミと画像のアップロードのみを行い、その後の分析やメール送信は、Amazon SQSを介して実行されるAWS Step Functionsのステートマシーンにより実行されます。

なお、webアプリは、streamlit　よりwebアプリを形成し、作成したREST APIをコールする(任意)
'''

# python言語用のシンタックスハイライトを表示する(コード上)
st.code(code, language='python')

st.subheader('自己紹介')
st.text('自己紹介としては・・・バイクが好きです\n'
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
        reviewText = st.text_input('レビューコメント')
        userName = st.text_input('お名前')
        mailAddress = st.text_input('メールアドレス')
        imagePath = st.text_input('画像ファイル名 ⇒ 工事中のため「file_test2.png」をコピペしてください')
        
        #ボタン      
        submit_btn = st.form_submit_button('送信')
        cansel_btn = st.form_submit_button('キャンセル')

        if submit_btn:
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
            