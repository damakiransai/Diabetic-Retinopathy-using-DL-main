# RetinaGuard - Diabetic Retinopathy Screening

A modern, AI-powered web application for binary classification of Diabetic Retinopathy (DR) from retinal fundus images.

## 🚀 Features

- **Flask Backend API** - RESTful API for model inference
- **Modern Frontend** - Beautiful, animated UI with drag-and-drop upload
- **Real-time Predictions** - Instant DR detection with probability scores
- **Risk Categorization** - Four-tier risk assessment (Low, Borderline, Moderate, High)
- **Privacy-First** - All processing happens locally on your machine

## 📋 Requirements

- Python 3.8+
- TensorFlow
- Flask
- Model file: `dr_binary_model.h5` (should be in project root)

## 🛠️ Installation

1. **Install dependencies:**
```powershell
pip install -r requirements.txt
```

2. **Ensure model file is present:**
   - Make sure `dr_binary_model.h5` is in the project root folder

## 🎯 Usage

### Quick Start

**Run the Flask server:**
```powershell
python flask_app.py
```

Or use the PowerShell script:
```powershell
.\run_flask.ps1
```

### Access Points

Once the server is running:

- **Landing Page:** http://localhost:5000/
- **Main App:** http://localhost:5000/app
- **API Endpoint:** http://localhost:5000/api/predict
- **Health Check:** http://localhost:5000/api/health

### Using the API

**POST Request to `/api/predict`:**
```bash
curl -X POST -F "image=@your_image.jpg" http://localhost:5000/api/predict
```

**Response:**
```json
{
  "success": true,
  "prediction": "DR Detected",
  "has_dr": true,
  "probability": 0.9112,
  "risk_category": "High Risk",
  "threshold": 0.4
}
```

## 📁 Project Structure

```
dldr/
├── flask_app.py          # Flask backend API
├── app.html              # Main application UI
├── index.html            # Landing page
├── dr_binary_model.h5    # TensorFlow model (required)
├── requirements.txt      # Python dependencies
├── run_flask.ps1         # PowerShell run script
└── README.md             # This file
```

## 🎨 UI Features

- **Animated Background** - Dynamic gradient backgrounds with floating particles
- **Drag & Drop Upload** - Easy image upload interface
- **Real-time Results** - Instant prediction display with animated meters
- **Risk Visualization** - Color-coded risk categories
- **Responsive Design** - Works on desktop and mobile devices

## 🔧 Model Details

- **Input Size:** 224 × 224 RGB
- **Preprocessing:** Normalized to 0-1 range
- **Threshold:** 0.4 (probability > 0.4 = DR Detected)
- **Output:** Binary classification (DR / No DR) with probability score

## ⚠️ Medical Disclaimer

This tool is for **research and educational purposes only**. It is not a substitute for professional medical diagnosis or treatment. Always consult with qualified healthcare professionals for medical advice.

## 📝 Notes

- The model loads once at server startup for optimal performance
- Images are processed in memory - no files are saved
- All processing happens server-side for privacy
- CORS is enabled for frontend-backend communication

## 🐛 Troubleshooting

**Model not found:**
- Ensure `dr_binary_model.h5` is in the project root folder
- Check file permissions

**Port already in use:**
- Change port in `flask_app.py` (line: `app.run(..., port=5000)`)
- Or stop the process using port 5000

**Import errors:**
- Run `pip install -r requirements.txt` again
- Ensure you're using Python 3.8+

---

Built with ❤️ for healthcare research
