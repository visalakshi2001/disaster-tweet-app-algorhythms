import streamlit as st





st.set_page_config(page_title="Disaster Tweet Management")

def main_page(keyword):

    st.markdown("<center><h1>🕊️ Tweet Analytics for Disaster & Calamity Management</h1></center>", unsafe_allow_html=True)

    st.write(keyword)


def sidebar_page():

    with st.sidebar:

        st.title("Fetch Tweets")

        keyword = st.text_input("Tweets from User, Hashtag, Term")
        btn = st.button("search")

        if btn:
            return keyword


if __name__ == "__main__":

    key = sidebar_page()
    main_page(keyword=key)