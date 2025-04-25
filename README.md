# Simulated SOC Responder Training Assistant

This Streamlit app simulates how a Tier 1 or Tier 2 security analyst might respond to a reported incident.

## Input Examples
- "Phishing email reported by user"
- "Suspicious login from foreign country"
- "Malware alert triggered on endpoint"
- "DDoS attempt detected on public website"

## Output Includes
- Triage assessment
- Action checklist
- Ticket note (internal)
- Suggested user response (if needed)

## Setup
1. Install dependencies:
```bash
pip install streamlit openai
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY='your-key-here'
```

3. Run:
```bash
streamlit run responder_ui.py
```

---

Built for cybersecurity education and incident response training.