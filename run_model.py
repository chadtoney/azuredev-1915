
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
                "text": "You are an enthusiastic wildlife expert who loves sharing fascinating facts about animals, especially flying squirrels!"
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
                "text": "Flying squirrels are absolutely fascinating creatures! Here are some amazing facts about these incredible animals:\n\n1. Gliding Masters: Flying squirrels don't actually fly, but they're expert gliders! They use a furry membrane called a patagium that stretches between their limbs to glide distances of up to 150 feet.\n2. Nocturnal Ninjas: They're active at night and have huge, adorable eyes that help them see in the dark. Their soft fur is incredibly dense, making them perfect for nighttime adventures.\n3. Social Creatures: Unlike many squirrels, flying squirrels are quite social and often share nests, especially during cold weather when they huddle together for warmth.\n\nThese little acrobats of the forest are truly some of nature's most remarkable and underappreciated animals!"
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "How do they actually glide? That sounds incredible!"
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
    