# Audio Transcript Summarizer

This is a Python script that uses the OpenAI Whisper model to automatically transcribe an audio file and then use GPT 3.5 to generate a summary of its content. It is designed to simplify the process of summarizing audio content for various use cases, such as podcast episode summaries or meeting minutes.

## Prerequisites

Before using this script, ensure you have the following:

- An OpenAI GPT-3 API key. You can obtain one by signing up for OpenAI and creating an API key.
- Whisper installed for transcribing audio.
- Python 3 installed on your machine.
- The OpenAI Python library installed. You can install it using pip:


## Usage

1. Clone this repository or create a new Python script.
2. Replace the `api_key` variable with your GPT-3 API key. You can obtain this key from OpenAI.
3. Make sure you have the audio file you want to transcribe. Replace `"School for tired teens - BBC News.mp3"` with the path to your audio file in the `audio_file` variable.
4. Adjust the `max_tokens` value in the `openai.ChatCompletion.create` function to control the length of the summary generated.

## How It Works

1. The script imports the necessary libraries, including the OpenAI Python library.

2. It initializes the OpenAI API client with your API key.

3. The audio file is opened and read in binary mode. You need to specify the path to your audio file here.

4. The script utilizes the OpenAI Audio API to transcribe the audio file. The result is stored in the `transcript` variable.

5. A conversation is constructed for the GPT-3 model. It begins with a system message that informs the model it is a helpful assistant and a user message asking to summarize the `transcript`.

6. The conversation is sent to the GPT-3.5 Turbo model to generate a summary.

7. The summary is extracted from the model's response, and it is printed to the console.

## Running the Script

To run the script, execute it with Python:

```bash
python your_script_name.py
