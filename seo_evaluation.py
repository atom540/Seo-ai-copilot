import streamlit as st
import requests
from bs4 import BeautifulSoup
import openai
from openai import AzureOpenAI

openai.api_key = st.secrets["OPENAI_API_KEY"]
ENDPOINT = "https://polite-ground-030dc3103.4.azurestaticapps.net/api/v1"
MODEL_NAME = "gpt-35-turbo"
API_VERSION = "2024-02-01"

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=openai.api_key,
    api_version=API_VERSION,
)


def generate_ai_recommendation(website_data):
    messages = [
        {
            "role": "system",
            "content": "You are an expert SEO analyst."
        },
        {
            "role": "user",
            "content": (
                f"Analyze the SEO performance of the following website and suggest actions to improve it:\n"
                f"URL: {website_data['url']}\n"
                f"\nSearch Console Queries:\n- " + "\n- ".join(website_data['search_console_queries']) +
                f"\n\nClick Through Rate (CTR): {website_data['click_through_rate']}%\n"
                f"\nTop Linked Pages:\n- " + "\n- ".join(website_data['top_linked_pages']) +
                f"\n\nTop Countries:\n- " + "\n- ".join(website_data['top_countries']) +
                "\n\nProvide a detailed analysis and recommendations for the following areas:\n"
                "1. **Content Optimization**: How can the content be improved to better match user intent and improve ranking?\n"
                "   Example: Identify key topics related to 'landing page best practices' and suggest specific improvements such as updating outdated content or adding multimedia elements.\n"
                "2. **Meta Tags**: How can meta titles and descriptions be optimized to improve CTR?\n"
                "   Example: Craft compelling meta titles using keywords like 'best landing page strategies' and ensure descriptions summarize content effectively.\n"
                "3. **Internal Linking**: Are there opportunities to improve internal linking for better navigation and SEO?\n"
                "   Example: Recommend linking related articles using anchor text 'landing page optimization tips' to improve user engagement.\n"
                "4. **Technical SEO**: Identify any technical issues that may be affecting the site's performance (e.g., page speed, mobile usability).\n"
                "   Example: Evaluate site speed metrics and suggest improvements such as optimizing images and leveraging browser caching.\n"
                "5. **Backlink Strategy**: Provide detailed recommendations for acquiring high-quality backlinks. Suggest potential partner websites for backlink opportunities and specify the exact pages that would be beneficial to link to.\n"
                "   Example: Propose guest blogging opportunities with authoritative sites in the digital marketing niche, emphasizing content relevance and value.\n"
                "6. **Local SEO**: Since the top country is India, what local SEO strategies should be implemented to better target the Indian audience?\n"
                "   Example: Optimize content with regional keywords like 'landing page best practices in India' and list the business on local directories.\n" 
                "7. **Competitor Analysis**: How does this website compare with its competitors in terms of SEO performance, and what strategies can be borrowed from competitors?\n"
                "   Example: Analyze competitor backlink profiles to identify gaps and suggest strategies for outperforming competitors in search rankings.\n"
                "\nBased on your analysis, rate the SEO performance of this website on a scale from 0 to 10.\n"
                "Provide an overall rating and actionable recommendations based on the assessment."
            )
        }
]


   
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        max_tokens=1500,   
        temperature=0.7,
          seed=42,
    )
    return response.choices[0].message.content
