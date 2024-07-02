# Telnyx-Hume AI Integration

This Flask application integrates Telnyx and Hume AI to process incoming calls, transcribe them, and respond using text-to-speech. The app handles events from Telnyx, sends transcriptions to Hume AI, and plays the AI's responses back to the caller.

## Features

- Answer incoming calls and start transcription.
- Send transcriptions to Hume AI for processing.
- Play responses from Hume AI back to the caller.
- End calls based on specific voice commands.

## Requirements

- Python 3.6+
- Flask
- Telnyx Python SDK
- Requests
- Websockets
- python-dotenv

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/telnyx-hume-ai-integration.git
   cd telnyx-hume-ai-integration
