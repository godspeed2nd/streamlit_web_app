# ローカル環境での起動方法
#        PS C:\temp\pythonProject1\streamlit\CloudTech_Splint7\sub> streamlit run 1_はじめに.py      

# https://www.youtube.com/watch?v=4nsTce1Oce8&t=1696s


import streamlit as st

st.title('Cloud Tech Academy')
st.caption('スプリント7の演習です ver 1.0')

# image = Image.open('/data/cloudtechacademy_logo.png')
# st.image(image, width=200)

st.subheader('はじめに')

code = '''
ユーザーが口コミのテキスト、画像、メールアドレス、氏名を入力すると、その内容が Amazon DynamoDB に保存されます。口コミテキストは Amazon Comprehend による感情分析が行われ、その結果に基づいてカスタマイズされたお礼メールが Amazon SES を通じて自動送信されます。また、送信された画像ファイルについては、S3バケットに保存されその後、 Amazon Rekognition による不適切な内容のチェックが行われます。

口コミの投稿は API Gateway 経由で API によって受け付けられます。API のレスポンスを高速化するため、API では口コミと画像のアップロードのみが行われ、感情分析やメール送信といった後続の処理は Amazon SQS を介した AWS Step Functions のステートマシンで非同期に実行されます。

さらに、Webアプリは Streamlit を利用して構築され、作成した REST API を任意でコールできます。Streamlit で使用する Python コードはローカルPCで開発し、GitHub に登録することで Streamlit との連携が可能です。これにより、VSCode を使ってローカルPCで開発したコードを GitHub 経由で更新し、Streamlit 上のアプリに反映させることができます。

参考
https://streamlit.io/
'''
# python言語用のシンタックスハイライトを表示する(コード上)
st.code(code, language='python')

# st.subheader('本サイトの構成')

# image = Image.open('./data/splint7_ensyou_kouseizu.png')
# st.image(image, width=1000)

# st.code(code, language='python')
