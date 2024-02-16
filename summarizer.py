from langchain_together import Together

class Summarizer:
    def __init__(self):
        self.llm = Together(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            temperature=0.8,
            max_tokens=512,
            top_k=1,
            together_api_key="a985c29ac716c499ebb9de7c125a15d984102855c1acd10ba9713403f94fc406"
        )

    def generate_summary(self, input_text):
        prompt = """
        You are a German text summarization model. Generate a concise summary of the above text in German language. Focus on key points and maintain clarity.
        """

        full_input = input_text + prompt
        output_summary = self.llm.invoke(full_input)
        return output_summary


