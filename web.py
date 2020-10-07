from requestbin import config
import os

from requestbin import app

if __name__ == "__main__":
    port = int(config.PORT)
    app.run(host='0.0.0.0', port=port, debug=config.DEBUG)