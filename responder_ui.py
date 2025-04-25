import streamlit as st
from openai import OpenAI

# Properly retrieve API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["openai_api_key"])

st.title("Simulated SOC Responder Training Assistant")
st.write("Paste a security incident scenario. Get simulated triage, response steps, and communication guidance.")

scenario = st.text_area("Incident Scenario (e.g. suspicious login, phishing email, malware alert)", height=200)

level = st.selectbox("Simulation Level", ["Junior Analyst", "Intermediate Responder", "Advanced Drill"])

if st.button("Simulate Response"):
    if not scenario.strip():
        st.warning("Please enter a scenario to simulate.")
    else:
        prompt = (
            f"Act as a {level} in a SOC team. Given this scenario, provide: "
            "- 1. Initial triage assessment\n"
            "- 2. Action steps\n"
            "- 3. Internal ticket note\n"
            "- 4. Suggested response to user (if relevant)\n"
            f"Scenario: {scenario}"
        )
        with st.spinner("Simulating response..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a cybersecurity incident responder trainer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6
            )
            answer = response.choices[0].message.content
            st.subheader("Simulated Response")
            st.write(answer)