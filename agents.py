import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

#  Get Gemini API key from .env
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(" GEMINI_API_KEY not found in .env file")

#  Initialize Gemini client
client = genai.Client(api_key=api_key)


def call_gemini(prompt: str) -> str:
    """
    Helper function to call Gemini API with a prompt.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"


# Definitions of agents
def email_agent(prompt: str) -> str:
    """Rewrites the message as a short, professional email."""
    return call_gemini(f"Rewrite this message as a short, professional email (2–3 lines max):\n{prompt}")


def ticket_agent(prompt: str) -> str:
    """Briefly classifies a support ticket with category, priority, and one-line action."""
    return call_gemini(f"Classify this support ticket. Respond briefly in this format:\n"
                       f"Category: ... | Priority: ... | Action: ...\n\nTicket: {prompt}")


def sentiment_agent(prompt: str) -> str:
    """Returns sentiment in one word: Positive / Negative / Neutral."""
    return call_gemini(f"Analyze sentiment of this text and reply with only one word "
                       f"(Positive, Negative, or Neutral):\n{prompt}")


def suggestion_agent(prompt: str) -> str:
    """Provides a one-line actionable suggestion for resolution."""
    return call_gemini(f"Give one short actionable suggestion (max 1 line) for resolving this issue:\n{prompt}")


# Types of agents
AGENTS = {
    "email_agent": email_agent,
    "ticket_agent": ticket_agent,
    "sentiment_agent": sentiment_agent,
    "suggestion_agent": suggestion_agent
}
