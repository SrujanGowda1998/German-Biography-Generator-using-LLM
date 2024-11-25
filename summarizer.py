from langchain_together import Together
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

class Summarizer:
    def __init__(self):
        self.llm = Together(
            # model = "mistralai/Mistral-7B-Instruct-v0.2",
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            # model = "snorkelai/Snorkel-Mistral-PairRM-DPO",
            temperature=0.1,
            max_tokens=512,
            top_k=1,
            # together_api_key = os.getenv("TOGETHER_API_KEY")
            together_api_key = st.secrets["together"]["together_api_key"]
        )


    def generate_summary(self, input_text):
        # prompt = """
        # You are a German text summarization model. Generate a concise summary of the above text in German language. Focus on key points and maintain clarity.
        # """
        prompt = """
        Du bist ein deutsches Textzusammenfassungsmodell. Erstellen Sie eine prägnante Zusammenfassung des obigen Textes in deutscher Sprache. Konzentrieren Sie sich auf die wichtigsten Punkte und bewahren Sie Klarheit.
        """
        full_input = input_text + prompt
        output_summary = self.llm.invoke(full_input)
        return output_summary
    

    def generate_biography(self, input_text):
        # prompt = """
        # Sie sind ein professioneller Biografieautor. Schreiben Sie eine Biografie der obigen Interviewzusammenfassung in deutscher Sprache. Konzentrieren Sie sich auf die wichtigsten Punkte und bewahren Sie Klarheit.
        # """
        prompt = """
        You are a professional biography author. Write a biography of the above interview summary in German language. Focus on key points and maintain clarity.
        """
        full_input = input_text + prompt
        output_summary = self.llm.invoke(full_input)
        print(output_summary)
        return output_summary



