from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load your TensorFlow model (replace 'path_to_your_model.h5' with the correct path)
model = tf.keras.models.load_model('path_to_our_tensorflow_model.h5')

@app.route('/')
def home():
    return "Sign Language Recognition API is running!"

# API endpoint for handling image uploads and making predictions
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    image_file = request.files['file']
    
    try:
        # Convert the uploaded image to a format TensorFlow can process
        image = Image.open(image_file)
        image = image.resize((224, 224))  # Resize image for the model
        image = np.array(image) / 255.0   # Normalize pixel values
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Make a prediction using the model
        prediction = model.predict(image)

        # Return the prediction result
        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
