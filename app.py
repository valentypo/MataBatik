import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
ASSETS_FOLDER = "assets"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

dic = {
    0: 'batik-bali', 1: 'batik-betawi', 2: 'batik-celup', 3: 'batik-cendrawasih',
    4: 'batik-ceplok', 5: 'batik-ciamis', 6: 'batik-garutan', 7: 'batik-gentongan',
    8: 'batik-kawung', 9: 'batik-keraton', 10: 'batik-lasem', 11: 'batik-megamendung',
    12: 'batik-parang', 13: 'batik-pekalongan', 14: 'batik-priangan', 15: 'batik-sekar',
    16: 'batik-sidoluhur', 17: 'batik-sidomukti', 18: 'batik-sogan', 19: 'batik-tambal'
}

def load_trained_model(model_path):
    if not os.path.exists(model_path):
        print(f"Error: Model file not found at {model_path}")
        return None
    try:
        model = load_model(model_path)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

model_path = "MataBatik-Batik Exception-46.93.h5" 
model = load_trained_model(model_path)

def predict_label(img_path):
    try:
        img = load_img(img_path, target_size=(224, 224))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array)
        class_idx = np.argmax(predictions)
        confidence = predictions[0][class_idx] * 100
        return dic[class_idx], round(confidence, 2)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Prediction error", 0

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/main")
def main():
    return render_template("Main_HTML.html")

@app.route("/detect", methods=["POST"])
def detect():
    if "my_image" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["my_image"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    if model:
        label, confidence = predict_label(file_path)
    else:
        label, confidence = "Model not loaded", 0

    return jsonify({
        "result": label,
        "confidence": f"{confidence}%",
        "image_url": f"/{file_path}"
    })

@app.route('/assets/<path:filename>')
def assets_files(filename):
    return send_from_directory('assets', filename)

if __name__ == "__main__":
    app.run(debug=True)
