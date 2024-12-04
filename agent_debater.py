import openai
from dotenv import load_dotenv

load_dotenv()

class Debater:
    def __init__(self, name):
        self.name = name

    def generate_opening_statement(self, topic):
        prompt = f"Generate a compelling opening statement for a debate on the topic: '{topic}'"
        return self._generate_argument(prompt)

    def generate_argument(self, topic):
        prompt = f"Generate a detailed argument for the debate topic: '{topic}'"
        return self._generate_argument(prompt)

    def _generate_argument(self, prompt):
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  # Use OpenAI's model for text generation
                prompt=prompt,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error generating response: {str(e)}"
