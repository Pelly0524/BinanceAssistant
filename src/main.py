from flask import Flask, request, abort
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage
from bot.line_bot import handle_message
from utils.config import Config

# Initialize the Flask application
app = Flask(__name__)

# Initialize the Line Bot Handler
handler = WebhookHandler(Config.LINE_CHANNEL_SECRET)


@app.route("/callback", methods=["POST"])
def callback():
    """Receive Line Bot Webhook requests"""
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    try:
        # Handle messages from Line
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"


# Handle messages of type TextMessage
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    handle_message(event)


if __name__ == "__main__":
    # Validate environment variables
    try:
        Config.validate()
        print("Environment variables validation passed ✅")

        # Starting Flask server
        print("Starting Flask server...")
        app.run(port=5000)

    except EnvironmentError as e:
        print(f"Environment variable error ❌: {e}")
