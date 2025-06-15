# MataBatik 🧵🔍

**MataBatik** is a web-based image classification project designed to identify and classify Indonesian batik patterns into one of 20 distinct categories. The platform combines a custom-trained deep learning model with a clean front-end interface, making traditional textile recognition accessible to everyone.

## 🧠 Features

- 📸 Upload batik images directly from your device
- 🧠 AI model classifies the image into 1 of 20 batik types
- 🔄 Real-time prediction using Flask backend
- 🌐 Fully responsive web interface
- ⚙️ Clear display of prediction results with batik name

---

## 🛠️ Tech Stack

### Frontend:
- **HTML / CSS / JavaScript**

### Backend & Model:
- **Python**
- **Flask**
- **TensorFlow / Keras**
- **YOLOv8 (used as image feature extractor)**

### Hosting:
- **Vercel** (frontend)
- **Railway** (backend and model deployment)

---

## 🚀 How It Works

1. A user uploads a batik image via the web interface.
2. The image is sent to the Flask backend.
3. A pre-trained YOLOv8 model extracts features.
4. Features are passed to a custom-trained sequential model.
5. The predicted batik type is returned and displayed to the user.

---

## 📂 Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/valentypo/MataBatik.git
   cd MataBatik

2. **Install backend dependencies**
  ```bash
  Copy
  Edit
  pip install -r requirements.txt
  Run Flask backend
  
  bash
  Copy
  Edit
  python app.py
  ```
3. **Open the index.html file in a browser**
   
⚠️ Make sure your .h5 model file is available and correctly referenced in app.py.

---
## 🙋‍♂️ Author
Steven Valentino Taslim

📧 stevenv2605@gmail.com

🔗 www.linkedin.com/in/steven-vt
