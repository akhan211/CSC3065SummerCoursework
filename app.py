from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

available_products = ["apple", "samsung", "kindle", "g-shock"]


@app.route("/check", methods=["POST"])
def check_product():
    data = request.get_json()
    product = data.get("product", "").lower()
    if product in available_products:
        return jsonify({"message": "Product is ready to manufacture"})
    else:
        return jsonify({"message": "Product is not available"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
