import streamlit as st
import openai
import time

# Use API key from Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

st.title("Simulated SOC Responder Training Assistant")
st.write("Paste a security incident scenario. Get simulated triage, response steps, and communication guidance.")

scenario = st.text_area("Incident Scenario (e.g. suspicious login, phishing email, malware alert)", height=200)

level = st.selectbox("Simulation Level", ["Junior Analyst", "Intermediate Responder", "Advanced Drill"])

if st.button("Simulate Response"):
    if not scenario.strip():
        st.warning("Please enter a scenario to simulate.")
    else:
        prompt = (
            f"Act as a {level} in a SOC team. Given this scenario, provide:\n"
            "- 1. Initial triage assessment\n"
            "- 2. Action steps\n"
            "- 3. Internal ticket note\n"
            "- 4. Suggested response to user (if relevant)\n"
            f"Scenario: {scenario}"
        )

        MAX_RETRIES = 3
        RETRY_DELAY = 5
        response = None

        for attempt in range(MAX_RETRIES):
            try:
                with st.spinner(f"Contacting OpenAI... (attempt {attempt + 1})"):
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=prompt,
                        max_tokens=800,
                        temperature=0.6
                    )
                break
            except openai.error.RateLimitError:
                st.warning(f"Rate limit hit. Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            except openai.error.OpenAIError as e:
                st.error(f"OpenAI API error: {str(e)}")
                break

        if response:
            answer = response.choices[0].text.strip()
            st.subheader("Simulated Response")
            st.write(answer)
        else:
            st.error("Failed to generate response after multiple retries.")