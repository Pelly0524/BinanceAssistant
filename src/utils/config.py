from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()


class Config:
    # Line Bot environment variables
    LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

    # Binance API environment variables
    BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
    BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

    # OpenAI LLM environment variables
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def validate():
        """Check if all required environment variables are correctly loaded"""
        required_vars = [
            "LINE_CHANNEL_SECRET",
            "LINE_CHANNEL_ACCESS_TOKEN",
            "BINANCE_API_KEY",
            "BINANCE_API_SECRET",
            "OPENAI_API_KEY",
        ]

        missing_vars = [var for var in required_vars if os.getenv(var) is None]
        if missing_vars:
            raise EnvironmentError(
                f"Missing the following environment variables: {', '.join(missing_vars)}"
            )


if __name__ == "__main__":
    try:
        # Validate environment variables
        Config.validate()
        print("Environment variables loaded successfully ✅")
        print(f"Line Channel Secret: {Config.LINE_CHANNEL_SECRET}")
        print(f"Binance API Key: {Config.BINANCE_API_KEY}")
        print(f"OpenAI API Key: {Config.OPENAI_API_KEY}")
    except EnvironmentError as e:
        print(f"Environment variable error ❌: {e}")
