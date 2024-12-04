import openai
import os
from dotenv import load_dotenv

# Load OpenAI API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class Debater:
    def __init__(self, name, viewpoint):
        self.name = name
        self.viewpoint = viewpoint
        self.memory = []  # Memory to track arguments
        self.opponent_memory = []  # Memory of the opponent's arguments
        self.turns = 0  # Track number of turns in the debate

    def generate_opening_statement(self):
        statement = self._generate_statement("opening", self.viewpoint)
        self.memory.append(statement)
        return statement

    def generate_main_argument(self):
        argument = self._generate_statement("main", self.viewpoint)
        self.memory.append(argument)
        return argument

    def generate_rebuttal(self, opponent_argument):
        rebuttal = self._generate_rebuttal_statement(opponent_argument)
        self.memory.append(rebuttal)
        return rebuttal

    def generate_closing_statement(self):
        closing = self._generate_statement("closing", self.viewpoint)
        self.memory.append(closing)
        return closing

    def _generate_statement(self, type_of_statement, viewpoint):
        prompt = f"Generate a concise {type_of_statement} statement(4-5 Sentences) supporting the viewpoint: {viewpoint}"
        return self._call_openai(prompt)

    def _generate_rebuttal_statement(self, opponent_argument):
        prompt = f"Generate a rebuttal (4-5 sentences) to the argument: {opponent_argument}"
        return self._call_openai(prompt)

    def _call_openai(self, prompt):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].text.strip()

    def perceive_opponent(self, opponent_statement):
        # Perception involves analyzing the opponent's statement and responding
        self.opponent_memory.append(opponent_statement)
        perceived_response = f"Perceived argument from opponent: {opponent_statement}. My counter-argument: {self._generate_rebuttal_statement(opponent_statement)}"
        return perceived_response

