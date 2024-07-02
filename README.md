
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
- WebSockets
- python-dotenv
- ngrok (for exposing local server to the internet)

## Installation

### Telnyx Setup 

1. Log in to your Telnyx Account
2. Purchase a number, if you haven't already
3. Create a Call Control Application by navigating to https://portal.telnyx.com/v2/index.html#/call-control/applications and create a new application with the appropriate settings.
4. Go to "Webhooks" under the "Connections" section and paste the ngrok URL followed by /webhook.
5. Assign the number to the Call Control Application on the numbers page

### Running the Code

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/telnyx-hume-ai-integration.git
    cd telnyx-hume-ai-integration
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the root directory with the following content:

    ```bash
    TELNYX_API_KEY=your_telnyx_api_key
    HUME_API_KEY=your_hume_api_key
    ```
5. **Expose Local Server to the Internet Using ngrok**

    Download and install ngrok. https://ngrok.com/docs/guides/
    Start ngrok on port 5000:
    ```bash
    ngrok http 5000
    ```
    Copy the generated public URL from the ngrok terminal. This URL will be used to set up the webhook in Telnyx.

6. **Run the Application**

    ```bash
    python app.py
    ```

## Usage

- The application listens for webhook events from Telnyx.
- Upon receiving a `call.initiated` event, it answers the call and starts transcription.
- Transcriptions are sent to Hume AI for processing, and responses are played back to the caller.
- The call can be ended by saying "hang", "hang up", or "end the call".
