from dotenv import load_dotenv
from google import genai

load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain what SAP is in simple terms."
)
print(response.text)