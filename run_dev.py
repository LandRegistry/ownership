from ownership.server import app
import os

app.run(host="0.0.0.0", port=9002, debug=True)

#int(os.environ['PORT']
