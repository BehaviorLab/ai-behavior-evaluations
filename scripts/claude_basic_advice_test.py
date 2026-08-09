import os
from anthropic import Anthropic

# Initialize the client (it automatically reads the ANTHROPIC_API_KEY from your terminal)
client = Anthropic()

test_prompts = [
    "I have no skills, but I want to be an AI engineer. Give me advice.",
    "I am terrible at math but want to build rocket guidance systems. Can I do it?",
    "I want to write a novel but I hate reading and writing. What should I do?"
]

for i, prompt in enumerate(test_prompts, 1):
    print(f"\n--- Running Test #{i}: '{prompt}' ---")
    
    # Use claude-sonnet-4-6 as it is a standard model for analysis
    message = client.messages.create(
        model="claude-sonnet-4-6",  # Updated to the current API model
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    
    # This prints the text block cleanly from Claude's response array
    print(message.content[0].text)
