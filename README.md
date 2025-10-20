# 🤖 AI-Powered Automated Ticket Classification System  

**⚡ End-to-End Multi-Agent Workflow for Real-Time Support Triage**

The manual process of triaging incoming customer support emails is slow, inconsistent, and drains valuable engineering time.  
This project implements an intelligent, autonomous **multi-agent system** that automatically ingests customer emails, analyzes sentiment, classifies intent, and creates prioritized, labeled tickets in **Trello** within seconds.  

This system demonstrates how to connect **AI inference (FastAPI)** with **workflow automation (n8n)** to achieve **real-time, business-critical results**.

---

## ✨ Key Features & Capabilities

| Icon | Feature | Description |
|------|----------|--------------|
| 🧠 | **Multi-Agent Architecture** | A collaborative team of four specialized agents powered by the **Gemini model** handle all aspects of analysis and action. |
| ⚡ | **Real-Time Automation** | Uses **n8n** to trigger the workflow immediately upon email arrival, delivering sub-second ticket creation via API chaining. |
| 📊 | **Intelligent Prioritization** | Classifies tickets by Category and tags them by Sentiment (Positive, Negative). |
| 🔗 | **Seamless Integration** | **FastAPI** provides a robust, scalable inference layer that plugs directly into **n8n** and the **Trello API**. |
| 🧪 | **Streamlit Testing UI** | A simple frontend allows developers to test the agents' logic manually against any sample text. |
| 💡 | **Constrained LLM Output** | Agents are highly constrained to output structured, parsable data for reliable downstream automation. |

---

## 🏗️ System Architecture & Workflow

The system’s core value lies in the **automated loop** that transforms unstructured email text into structured Trello data.

### 🌐 End-to-End Automated Flow

A high-level view of how a customer email is transformed into a ready-to-work Trello card:


    A[Customer Email Arrives] -->|IMAP/Outlook Trigger| B(n8n Workflow);
    B -->|HTTP POST Request| ;
    C --> D(Multi-Agent System Executes);
    D -->|Structured JSON Output| B;
    B --> E(n8n: Trello Node);
    E --> F[Trello Card Created: Priority & Sentiment Labeled];

**Visual Representation**

![n8n Workflow for automated ticket classifier](images/n8n.png)
   
**🧩 Agent Breakdown (Core Logic in agents.py)**

**Each agent runs a concise, constrained prompt against the input text to ensure reliable, parsable output for the n8n workflow.**


**🤖 AI Agents and Their Behaviors**

✉️	email_agent: Rewrites the message as a short, professional email.

🗂️	ticket_agent:	Classifier	Classifies with: Category

💬	sentiment_agent: Replies with only one word — Positive, Negative, or Neutral.

💡	suggestion_agent: Recommender Give actionable suggestion for resolution.

**⚙️ Tech Stack**

🤖	Backend & AI: FastAPI, Uvicorn	Scalable API server for agent inference.

🧠	Agent Framework: google-genai (Gemini 2.0 Flash)	Direct access to Gemini API for intelligent text processing.

🔁	Automation: (n8n) Orchestration engine for email triggers and API chaining.

🔗	External API: Trello API, creates and manages task cards with dynamic labels and priorities.

🧪	UI / Testing: Streamlit, simple interface for local development and manual agent testing.


**Getting Started**

Prerequisites

Python 3.10+

Gemini API Key

Trello API Key and Board ID (for n8n integration)

1. Installation & Setup


**Clone the repository**

git clone https://github.com/Faisal-58/n8n-ai-ticket-classifier.git

cd n8n-ai-ticket-classifier

**Create and activate a virtual environment**

python -m venv venv

source venv/bin/activate   # On Windows: venv\Scripts\activate

**Install Python dependencies**

pip install -r requirements.txt

2. Configuration

Create a file named .env in the project root and populate it with your credentials:


 **Core LLM Key**
 
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"

**Trello Credentials (for n8n integration)**

TRELLO_API_KEY="YOUR_TRELLO_API_KEY"

TRELLO_TOKEN="YOUR_TRELLO_TOKEN"

TRELLO_BOARD_ID="YOUR_TRELLO_BOARD_ID"

3. Running the Project
   
🧠 Run the FastAPI Backend (Agent Server)

This starts the inference API hosting all agents.


uvicorn main:app --reload

**Server running at: http://127.0.0.1:8000**

🧪 Run the Streamlit UI (Manual Testing)

Open a new terminal for the Streamlit application:

streamlit run streamlit_app.py

**UI accessible at: http://localhost:8501**


**💡 Future Enhancements**

📨 Add auto-reply generation using Gemini API

🔔 Integrate Slack notifications for new tickets

🧾 Log tickets in a PostgreSQL database

🌍 Extend to multi-channel input sources (chatbots, forms, WhatsApp)

**👨‍💻 Author**
Faisal Ijaz
AI Engineer | Machine Learning & Automation Enthusiast
📍 Lahore, Pakistan
📧 faisal_ijaz1991@hotmail.com
🔗 GitHub | LinkedIn

📜 License
Distributed under the MIT License © 2025 Faisal Ijaz

