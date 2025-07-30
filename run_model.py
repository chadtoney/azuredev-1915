
import openai
import os
import base64
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

endpoint = os.getenv("ENDPOINT_URL", "https://prepareforanaidevproj-resource.cognitiveservices.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

# Validate that required environment variables are set
if not subscription_key:
    raise ValueError("AZURE_OPENAI_API_KEY environment variable is required but not set")

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# IMAGE_PATH = "YOUR_IMAGE_PATH"
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')

# Prepare the chat prompt
chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are an enthusiastic wildlife expert who specializes in flying squirrels and loves sharing fascinating facts about these amazing creatures."
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Tell me about flying squirrels! What makes them so amazing?"
            }
        ]
    },
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "Flying squirrels are absolutely extraordinary creatures! They're some of nature's most skilled gliders and have several amazing adaptations that make them truly special:\n\n1. **Patagium Magic**: They have a furry membrane called a patagium that stretches from their wrists to their ankles, allowing them to glide up to 150 feet through the forest canopy!\n\n2. **Night Vision Superpowers**: Their large, dark eyes are perfectly adapted for nocturnal life, giving them excellent night vision to navigate in complete darkness.\n\n3. **Soft Landing Specialists**: They use their fluffy, rudder-like tail to steer and brake during glides, making precision landings on tree trunks with remarkable accuracy.\n\nThese acrobatic mammals are found on every continent except Antarctica and Australia, and despite their name, they don't actually fly - they're master gliders who can change direction mid-flight!"
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "How far can they actually glide? That sounds incredible!"
            }
        ]
    }
]

# Include speech result if speech is enabled
messages = chat_prompt

# Generate the completion
completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

print(completion.to_json())
    