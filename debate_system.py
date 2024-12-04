import streamlit as st
from agent_debater import Debater

# Initialize debaters
debater_1 = Debater(name="Debater 1", viewpoint="Climate Change is caused by human activity")
debater_2 = Debater(name="Debater 2", viewpoint="Climate Change is a natural occurrence")

# Function to control the flow of the debate
def run_debate():
    # Initialize debate
    st.title("AI Debate Simulation")
    st.write("This is an AI-powered debate between two debaters.")
    
    # Generate Opening Statements
    st.subheader("Opening Statements")
    opening_1 = debater_1.generate_opening_statement()
    opening_2 = debater_2.generate_opening_statement()
    st.write(f"**{debater_1.name}'s Opening Statement**: {opening_1}")
    st.write(f"**{debater_2.name}'s Opening Statement**: {opening_2}")

    # Main Arguments Phase
    st.subheader("Main Arguments")
    main_1 = debater_1.generate_main_argument()
    main_2 = debater_2.generate_main_argument()
    st.write(f"**{debater_1.name}'s Main Argument**: {main_1}")
    st.write(f"**{debater_2.name}'s Main Argument**: {main_2}")

    # Rebuttals Phase
    st.subheader("Rebuttals")
    rebuttal_1 = debater_1.generate_rebuttal(main_2)
    rebuttal_2 = debater_2.generate_rebuttal(main_1)
    st.write(f"**{debater_1.name}'s Rebuttal**: {rebuttal_1}")
    st.write(f"**{debater_2.name}'s Rebuttal**: {rebuttal_2}")

    # Closing Statements Phase
    st.subheader("Closing Statements")
    closing_1 = debater_1.generate_closing_statement()
    closing_2 = debater_2.generate_closing_statement()
    st.write(f"**{debater_1.name}'s Closing Statement**: {closing_1}")
    st.write(f"**{debater_2.name}'s Closing Statement**: {closing_2}")

    # End of Debate
    st.write("The debate has ended.")

# Running the debate
if __name__ == "__main__":
    run_debate()
