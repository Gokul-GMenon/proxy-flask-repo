from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# On the external server (e.g. Flask API):
@app.route("/proxy_image", methods=['GET'])
def proxy():
    image_url = request.args.get("url")
    img_resp = requests.get(image_url)
    img = img_resp.content
    return Response(img, mimetype=img_resp.headers.get("Content-Type", "image/png"))


if __name__ == '__main__':
    app.run(debug=True)
