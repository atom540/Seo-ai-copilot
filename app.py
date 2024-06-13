import streamlit as st
import pandas as pd
import numpy as np


from seo_evaluation import generate_ai_recommendation


st.title('SEO Analysis and Recommendations')
st.sidebar.title('User Inputs')



def main():
    # st.title('SEO Analysis Questions')
    
    # Collect user inputs
    url = st.text_input('Enter the website URL:')
    search_console_queries = st.text_area('Enter Search Console queries (comma-separated):')
    click_through_rate = st.slider('Click Through Rate (CTR)', 2.0, 10.0)
    top_linked_pages = st.text_area('Enter Top Linked Pages (comma-separated):')
    top_countries = st.text_area('Enter Top Countries (comma-separated):')

    website_data = {
        'url': url,
        'search_console_queries': search_console_queries.split(','),
        'click_through_rate': click_through_rate,
        'top_linked_pages': top_linked_pages.split(','),
        'top_countries': top_countries.split(',')
        }
    # st.write(website_data)
    # Button to submit inputs
    if st.button('Submit'):
        ai_response = generate_ai_recommendation(website_data)
        st.write('AI Recommendation:')
        st.write(ai_response)

        if st.button('Clear Response'):
            st.empty()  # Clears the output area
        elif st.button('Fill New Data'):
            st.text_input('Enter the website URL:')
            st.text_area('Enter Search Console queries (comma-separated):')
            st.slider('Click Through Rate (CTR)', 2.0, 10.0)
            st.text_area('Enter Top Linked Pages (comma-separated):')
            st.text_area('Enter Top Countries (comma-separated):')

if __name__ == '__main__':
    main()



