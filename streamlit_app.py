import streamlit as st
import requests


st.set_page_config(page_title="🤖 Multi-Agent AI System", layout="wide")

# Custom CSS Styling
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #141E30, #243B55);
}
.main-title {
    text-align: center;
    font-size: 2.4rem;
    font-weight: 800;
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
}
.subtext {
    text-align: center;
    color: #475569;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

/* Input and buttons */
div[data-testid="stTextArea"] textarea {
    border-radius: 12px;
    font-size: 0.95rem;
}
div.stButton > button {
    background: linear-gradient(90deg, #2563eb 0%, #3b82f6 100%);
    color: white;
    font-weight: 600;
    border-radius: 10px;
    padding: 0.6rem 1.4rem;
    transition: all 0.3s ease-in-out;
}
div.stButton > button:hover {
    background: linear-gradient(90deg, #1d4ed8 0%, #2563eb 100%);
    transform: scale(1.03);
}

/* Agent cards */
.agent-card {
    padding: 1.1rem;
    border-radius: 14px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    margin-bottom: 1.2rem;
    transition: 0.3s;
}
.agent-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
}
.email {background-color: #eff6ff; border-left: 6px solid #3b82f6;}
.ticket {background-color: #ecfdf5; border-left: 6px solid #10b981;}
.sentiment {background-color: #fef9c3; border-left: 6px solid #f59e0b;}
.suggestion {background-color: #fef2f2; border-left: 6px solid #ef4444;}

.agent-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 0.4rem;
}
.agent-response {
    background-color: white;
    padding: 0.9rem;
    border-radius: 10px;
    color: #334155;
    font-size: 0.95rem;
    white-space: pre-line;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<h1 class='main-title'>🤖 Multi-Agent AI System</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Analyze, rewrite, and classify customer tickets using Gemini-powered AI agents.</p>", unsafe_allow_html=True)


FASTAPI_URL = "http://127.0.0.1:8000/agent"


prompt = st.text_area(" Enter your text or ticket:", height=140, placeholder="e.g. Customer thanked us for resolving their billing issue promptly.")

available_agents = ["email_agent", "ticket_agent", "sentiment_agent", "suggestion_agent"]
selected_agents = st.multiselect(" Select agents to use:", available_agents, default=available_agents)


if st.button(" Run AI Agents"):
    if not prompt.strip():
        st.warning(" Please enter a prompt before submitting.")
    elif not selected_agents:
        st.warning(" Please select at least one agent.")
    else:
        payload = {"agents": selected_agents, "prompt": prompt}

        with st.spinner("🤖 Running AI agents... please wait..."):
            try:
                response = requests.post(FASTAPI_URL, json=payload)
                if response.status_code == 200:
                    data = response.json()

                    st.markdown("---")
                    st.subheader(" Input Prompt")
                    st.info(data["prompt"])

                    st.markdown("###  Agent Responses")
                    for agent, result in data["results"].items():
                        color_class = {
                            "email_agent": "email",
                            "ticket_agent": "ticket",
                            "sentiment_agent": "sentiment",
                            "suggestion_agent": "suggestion"
                        }.get(agent, "")

                        st.markdown(
                            f"""
                            <div class="agent-card {color_class}">
                                <div class="agent-title">{agent.replace('_', ' ').title()}</div>
                                <div class="agent-response">{result}</div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                else:
                    st.error(f" Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f" Request failed: {e}")
