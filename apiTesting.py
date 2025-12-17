from dotenv import load_dotenv
import os
import google.genai as genai
import json

# Load .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file!")

# Configure API client
client = genai.Client(api_key=api_key)

# Model selection
model_name = "gemma-3-27b-it" 

file_path = os.path.join("database_logic", "ai_data.json")
with open(file_path, 'r') as f:
    data = json.load(f)

# Your test prompt
prompt = f"Using the data provided, Embody this type of person and act completely like him, answering questions like he would. What phone provider do you use? ONLY answer just an answer, don't make it like a conversation or a sentence, only a pure answer: {json.dumps(data)}"

# Make the request
response = client.models.generate_content(
    model=model_name,
    contents=prompt,
)

# Print the response
print("Gemini 2.5 response:")
print(response.text)

