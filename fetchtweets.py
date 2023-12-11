import ntscraper
import streamlit as st


@st.cache_resource
def tweet_object(skip_check=False):
    
    scraper = ntscraper.Nitter(skip_instance_check=skip_check)

    return scraper



def fetch_tweets(keyword, mode, number, near=None, exclude=None, filters=None, to=None, language='en', since=None, until=None):

    scraper = tweet_object()

    try:
        tweet_dict = scraper.get_tweets(keyword, mode=mode, number=number,
                                        near=near, exclude=exclude, filters=filters,
                                        to=to, language=language, since=since, until=until,
                                        # instance="http://localhost:8080"
                                        )
    except Exception as e:
        st.write("Retry request")
        print(e)

    # print(keyword, mode, number, to, near, since, until)

    return tweet_dict

def get_location():
    pass