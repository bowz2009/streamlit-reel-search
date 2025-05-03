
import streamlit as st
import pandas as pd

# CSVファイルの読み込み
df = pd.read_csv("cleaned_reels_list.csv")

# タイトル
st.title("ボウズのインスタリール案内所")

# 説明文
st.markdown("""
このページでは、ボウズこと安部雅道がこれまでに投稿してきた  
インスタのリール動画をキーワードで検索することができます。  
「氣虚」「PMS」「人間関係」など、気になる言葉を入力してみてください。
""")

# 検索ボックスのラベル
keyword = st.text_input("🔍 キーワードを入力してください")

# 検索処理
if keyword:
    st.markdown("---")
    results = df[
        df["タイトル"].str.contains(keyword, case=False, na=False) |
        df["グループ"].str.contains(keyword, case=False, na=False) |
        df["症状名・悩み事"].str.contains(keyword, case=False, na=False)
    ]
    
    if not results.empty:
        st.success(f"{len(results)} 件のリールが見つかりました：")
        for _, row in results.iterrows():
            st.markdown(f"**タイトル：** {row['タイトル']}")
            st.markdown(f"**投稿日：** {row['投稿日']}")
            st.markdown(f"**URL：** [Instagramで見る]({row['URL']})")
            st.markdown("---")
    else:
        st.warning("該当するリールは見つかりませんでした。")
