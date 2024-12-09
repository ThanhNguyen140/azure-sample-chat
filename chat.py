import os
import openai

openai.api_type = "azure"
# Enter deployment endpoint
openai.api_base = "https://phuon-m49vh17t-eastus2.cognitiveservices.azure.com/"
openai.api_version = "2024-08-01-preview"
# Enter deployment key
openai.api_key = "******************"


def ai_chat(user_message):
    message_text = [
       {"role":"system","content":"You are an AI assistant that helps people find information."},
       {"role": "user", "content": user_message}
    ]

    completion = openai.ChatCompletion.create(
      engine="gpt-35-turbo-16k",
      messages=message_text,
      temperature=0.8,
      max_tokens=1000,
      top_p=0.95,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None
    )
    return completion

if __name__ == "__main__":
  print("Welcome! I am AI assistant. How can I help you today?")

  while True:
      user_message = input(">> ")
      completion = ai_chat(user_message)
      # Completion will return a response that we need to use to get the acctual string
      print(completion['choices'][0]['message']['content'])
