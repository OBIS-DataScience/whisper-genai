import openai
# Your OpenAI GPT-3 API key
api_key = "OPEN_AI_KEY"

# Initialize the OpenAI API client
openai.api_key = api_key
# import audio file
audio_file= open("School for tired teens - BBC News.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

# Initialize a conversation with a system message
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": f"Summarize the following text: \"{transcript}\""}
]

# Request the summary using the chat model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation,
    max_tokens=50,  # Adjust the number of tokens as needed
    api_key=api_key
)

# Extract and print the assistant's reply (summary)
summary = response['choices'][0]['message']['content']
print("Summary:", summary)
