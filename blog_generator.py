# Creating this project, I used OpenAI help and Codedex guide to create this project in the .env file. I added the API code through this file is API code, which I will not share in this file. In this file is -> API_KEY = api code line
from openai import OpenAI          # Import the OpenAI client
from dotenv import dotenv_values    # Import dotenv to read our API key from .env 

# ---------------------------- Load API key --------------------
config = dotenv_values(".env")                     # Read key/value pairs from .env
client = OpenAI(api_key=config["API_KEY"])         # Create the client with our API key

# ---------------------- Function that talks to OpenAI ----------
def generate_blog(paragraph_topic: str) -> str:
    prompt = f"Write a paragraph about the following topic: {paragraph_topic}"  # Build prompt
    response = client.chat.completions.create(      # Send prompt to OpenAI
        model="gpt-4.1-mini",                       # Current chat model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,                              # Max length of the reply
        temperature=0.3                               # Lower = more focused
    )
    return response.choices[0].message.content      # Return the generated paragraph

# ------------------------- Interactive loop -------------------
while True:
    answer = input("Write a paragraph? Y for yes, anything else for no: ").strip().lower()
    if answer == "y":
        topic = input("What should this paragraph talk about? ")
        print("\n--- Generated Paragraph ---\n")
        print(generate_blog(topic))
        print("\n---------------------------\n")
    else:
        print("Goodbye!")

        break
