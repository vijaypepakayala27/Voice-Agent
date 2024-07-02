import telnyx
import os
from flask import Flask, request, jsonify
import base64
import asyncio
import websockets
import json
import requests
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# Set up the Telnyx API key
TELNYX_API_KEY = os.getenv("TELNYX_API_KEY")
telnyx.api_key = TELNYX_API_KEY

# Hume API key
HUME_API_KEY = os.getenv("HUME_API_KEY")

async def send_to_hume(text):
    print(f"Sending text to Hume: {text}")
    uri = "wss://api.hume.ai/v0/evi/chat"
    headers = {
        "X-Hume-Api-Key": HUME_API_KEY
    }
    async with websockets.connect(uri, extra_headers=headers) as websocket:
        message = {
            "type": "user_input",
            "text": text
        }
        await websocket.send(json.dumps(message))
        print("Message sent to Hume, waiting for responses...")

        response_text = ""
        while True:
            response = await websocket.recv()
            response_data = json.loads(response)

            if response_data.get("type") == "assistant_message":
                reply = response_data.get("message")
                response_text += reply.get('content') + " "

            elif response_data.get("type") == "assistant_end":
                print("End of assistant messages.")
                break

        return response_text.strip()

def speak_text(call_control_id, text):
    print(f"Speaking text on call {call_control_id}: {text}")
    api_url = f"https://api.telnyx.com/v2/calls/{call_control_id}/actions/speak"
    headers = {
        "Authorization": f"Bearer {TELNYX_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "payload": text,
        "payload_type": "text",
        "voice": "female",
        "language": "en-US"
    }
    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Text to speech played successfully.")
    else:
        print(f"Failed to play text to speech: {response.status_code}, {response.text}")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json.get('data')

    if data.get('record_type') == 'event':
        event = data.get('event_type')
        call_control_id = data.get('payload').get('call_control_id')
        my_call = telnyx.Call()
        my_call.call_control_id = call_control_id
        print(f"Event: {event}, Call Control ID: {call_control_id}")

        if event == 'call.initiated':
            direction = data.get('payload').get('direction')

            if direction == 'incoming':
                encoded_client_state = base64.b64encode(direction.encode('ascii'))
                client_state_str = str(encoded_client_state, 'utf-8')
                res = my_call.answer(client_state=client_state_str)
                print(f"Call answered: {res}", flush=True)
                my_call.transcription_start(language="en")

        elif event == 'call.transcription':
            transcription = data.get('payload').get('transcription_data').get("transcript")
            print(f"Transcription: {transcription}")
            if transcription in ["hang", "hang up", "end the call"]:
                my_call.hangup()
            else:
                response_text = asyncio.run(send_to_hume(transcription))
                print(f"Response from Hume AI: {response_text}")
                if response_text:
                    speak_text(call_control_id, response_text)

        return jsonify({"status": "success"})

    return jsonify({"status": "ignored"}), 200

if __name__ == '__main__':
    app.run(port=5000)
