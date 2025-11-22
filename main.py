import streamlit as st # フロントエンドを扱うstreamlitの機能をインポート
from openai import OpenAI # openAIのchatGPTのAIを活用するため
import os # OSの機能をインポート

OPENAI_API_KEY = st.secret["openai"]["api_key"]


client = OpenAI(api_key=OPENAI_API_KEY)

def run_gpt(content_text_to_gpt,content_kind_of_to_gpt,content_maxStr_to_gpt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content":f"以下の条件に従って文章を作成してください。\
                \n\n条件1: {content_text_to_gpt}\
                \n条件2: {content_kind_of_to_gpt}\
                \n条件3: 文章の最大文字数は{content_maxStr_to_gpt}文字以内にしてください。"}
        ]
    )
    return response.choices[0].message.content.strip()

print('GPTに記事を書かせる')

content_text_to_gpt = st.text_input('記事の内容を入力してください。例：AIの未来について')
content_maxStr_to_gpt = str(st.slider('文章の最大文字数を入力してください。例：500', min_value=100, max_value=2000, step=100))
# テイストの種類を変更できるようにする
content_kind_of =[
    "中立的で客観的な文章",
    "分かりやすい、簡潔な文章",
    "親しみやすいトーンの文章",
    "専門用語をできるだけ使わない、一般読者向けの文章",
    "言葉の使い方にこだわり、正確な表現を心がけた文章",
    "ユーモアを交えた文章",
    "シンプルかつわかりやすい文法を使った文章",
    "面白く、興味深い内容を伝える文章",
    "具体的でイメージしやすい表現を使った文章",
    "人間味のある、感情や思いを表現する文章",
    "引用や参考文献を適切に挿入した、信頼性の高い文章",
    "読み手の興味を引きつけるタイトルやサブタイトルを使った文章",
    "統計データや図表を用いたわかりやすい文章",
    "独自の見解や考え方を示した、論理的な文章",
    "問題提起から解決策までを網羅した、解説的な文章",
    "ニュース性の高い、旬なトピックを取り上げた文章",
    "エンターテイメント性のある、軽快な文章",
    "読者の関心に合わせた、専門的な内容を深く掘り下げた文章",
    "人物紹介やインタビューを取り入れた、読み物的な文章",
]

content_kind_of_to_gpt = st.selectbox('文章のテイストを選んでください。', content_kind_of)
if st.button('記事作成'):
    with st.spinner('記事を作成中...しばらくお待ちください。'):
        gpt_message = run_gpt(content_text_to_gpt,content_kind_of_to_gpt,content_maxStr_to_gpt)
    st.success('記事が完成しました！')
    st.write(gpt_message)