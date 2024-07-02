# Voice-Agent
This Flask application integrates Telnyx and Hume AI to process incoming calls, transcribe them, and respond using text-to-speech. The app handles events from Telnyx, sends transcriptions to Hume AI, and plays the AI's responses back to the caller.
Features
Answer incoming calls and start transcription.
Send transcriptions to Hume AI for processing.
Play responses from Hume AI back to the caller.
End calls based on specific voice commands.
Requirements
Python 3.6+
Flask
Telnyx Python SDK
Requests
Websockets
python-dotenv
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/telnyx-hume-ai-integration.git
cd telnyx-hume-ai-integration
Create and Activate a Virtual Environment

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables
Create a .env file in the root directory with the following content:

makefile
Copy code
TELNYX_API_KEY=your_telnyx_api_key
HUME_API_KEY=your_hume_api_key
Run the Application

bash
Copy code
python app.py
Usage
The application listens for webhook events from Telnyx.
Upon receiving a call.initiated event, it answers the call and starts transcription.
Transcriptions are sent to Hume AI for processing, and responses are played back to the caller.
The call can be ended by saying "hang", "hang up", or "end the call".
