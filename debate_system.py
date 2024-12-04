import streamlit as st
from agent_debater import Debater
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Debater agents
debater1 = Debater("Debater 1")
debater2 = Debater("Debater 2")

st.title("AI Debate System")
debate_topic = st.text_input("Enter debate topic:", "Should AI be regulated by law?")

if debate_topic:

    st.subheader("Opening Statements")
    opening_statement1 = debater1.generate_opening_statement(debate_topic)
    opening_statement2 = debater2.generate_opening_statement(debate_topic)

    st.write(f"**{debater1.name}'s Opening Statement**: {opening_statement1}")
    st.write(f"**{debater2.name}'s Opening Statement**: {opening_statement2}")


    st.subheader("Main Arguments")
    argument1 = debater1.generate_argument(debate_topic)
    argument2 = debater2.generate_argument(debate_topic)

    st.write(f"**{debater1.name}'s Main Argument**: {argument1}")
    st.write(f"**{debater2.name}'s Main Argument**: {argument2}")
