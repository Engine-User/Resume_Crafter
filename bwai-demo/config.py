import os
from dotenv import load_dotenv

load_dotenv()

# --- Groq API Configuration ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("🔴 Groq API Key not found. Please ensure GROQ_API_KEY is set in your .env file.")

MODEL_NAME = "llama-3.3-70b-versatile"
