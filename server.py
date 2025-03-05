import os
import logging
from flask import Flask

app = Flask(__name__)

# Enable Debug Logging
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def home():
    app.logger.info("Home route accessed")
    return "Hello, Railway!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Ensure PORT is set
    app.run(host="0.0.0.0", port=port, debug=True)
