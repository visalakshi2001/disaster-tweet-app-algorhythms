import streamlit as st
import pandas as pd
from twitter_api_test import save_tweets
from twitter_api_test import scraper
st.set_page_config(page_title="Disaster Tweet Management")

def main_page(keyword):
    tweet = pd.read_csv("saved_tweets.csv")
    st.markdown("<center><h1>🕊️ Tweet Analytics for Disaster & Calamity Management</h1></center>", unsafe_allow_html=True)


    for user in tweet['user'].unique():
        user_texts = tweet[tweet['user'] == user]['text']
        user_link = tweet[tweet['user'] == user]['link']
        with st.container(border=True):
            col1, col2, col3 = st.columns(3)

            with col1:
                st.subheader("User")
                st.write(user)

            with col2:
                st.subheader("Tweet")
                for text in user_texts:
                    st.write(text)

            with col3:
                st.subheader("Link")
                for link in user_link:
                    st.write(link)


def sidebar_page():

    with st.sidebar:

        st.title("Fetch Tweets")

        keyword = st.text_input("Tweets from User, Hashtag, Term")
        btn = st.button("search")

        if btn:
            tweets = scraper.get_tweets(terms=keyword, mode='hashtag', number=10, near='usa', exclude=['nativeretweets'], language='en')
            save_tweets(tweets, topic=keyword)
            return keyword



if __name__ == "__main__":

    key = sidebar_page()
    main_page(keyword=key)