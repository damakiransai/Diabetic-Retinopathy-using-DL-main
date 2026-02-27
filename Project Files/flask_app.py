"""
Flask backend API for Diabetic Retinopathy Binary Classification
"""
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Global model variable
model = None

def load_dr_model():
    """Load the DR model once at startup"""
    global model
    if model is None:
        model_path = "dr_binary_model.h5"
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        model = load_model(model_path)
        print(f"✅ Model loaded successfully from {model_path}")
    return model

def preprocess_image(image: Image.Image, target_size=(224, 224)):
    """Preprocess image for model input"""
    image = image.convert("RGB")
    image = image.resize(target_size)
    img_array = np.array(image, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def get_risk_category(prob: float) -> str:
    """Get risk category based on probability"""
    if prob < 0.2:
        return "Low Risk"
    if prob <= 0.4:
        return "Borderline"
    if prob <= 0.7:
        return "Moderate Risk"
    return "High Risk"

@app.route('/')
def index():
    """Serve the landing page"""
    return send_from_directory('.', 'index.html')

@app.route('/app')
def app_page():
    """Serve the main app page"""
    return send_from_directory('.', 'app.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    """API endpoint for DR prediction"""
    try:
        # Check if file is present
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Validate file type
        allowed_extensions = {'jpg', 'jpeg', 'png'}
        file_ext = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''
        if file_ext not in allowed_extensions:
            return jsonify({'error': f'Invalid file type. Allowed: {", ".join(allowed_extensions)}'}), 400
        
        # Read and preprocess image
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        # Load model and predict
        model = load_dr_model()
        input_tensor = preprocess_image(image)
        prob = float(model.predict(input_tensor, verbose=0)[0][0])
        
        # Determine prediction
        threshold = 0.4
        has_dr = prob > threshold
        
        # Get risk category
        risk_category = get_risk_category(prob)
        
        # Return results
        return jsonify({
            'success': True,
            'prediction': 'DR Detected' if has_dr else 'No DR',
            'has_dr': has_dr,
            'probability': round(prob, 4),
            'risk_category': risk_category,
            'threshold': threshold
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    try:
        model = load_dr_model()
        return jsonify({
            'status': 'healthy',
            'model_loaded': model is not None
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    # Load model at startup
    print("🚀 Starting Flask server...")
    print("📦 Loading DR model...")
    try:
        load_dr_model()
        print("✅ Server ready!")
        print("🌐 App available at: http://localhost:5000")
        print("📄 Landing page: http://localhost:5000/")
        print("🔬 Main app: http://localhost:5000/app")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        exit(1)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
