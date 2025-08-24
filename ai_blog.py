#it prints one para by default and write multiple by entering a number
from openai import OpenAI
from dotenv import dotenv_values
import os

# Load API key from .env
config = dotenv_values(".env")
client = OpenAI(api_key=config["OPENAI_API_KEY"])

def generate_blog(paragraph_topic, num_paragraphs=1):
    """
    Generate a blog paragraph or multiple paragraphs.
    :param paragraph_topic: Topic to write about
    :param num_paragraphs: Number of paragraphs to generate
    """
    prompt = f"Write {num_paragraphs} paragraph{'s' if num_paragraphs > 1 else ''} about the following topic: {paragraph_topic}"

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",  # You can switch to gpt-4o-mini if you want
        prompt=prompt,
        max_tokens=400 * num_paragraphs,  # Increase tokens for multiple paragraphs
        temperature=0.3
    )
    return response.choices[0].text.strip()


# -------------------- User Interaction --------------------

keep_writing = True

while keep_writing:
    answer = input("Write a paragraph? Y for yes, anything else for no: ").upper()
    if answer == "Y":
        topic = input("What should this paragraph talk about? ")
        num = input("How many paragraphs? (default 1): ")
        try:
            num_paragraphs = int(num) if num else 1
        except ValueError:
            num_paragraphs = 1

        print("\n" + generate_blog(topic, num_paragraphs) + "\n")
    else:
        keep_writing = False
