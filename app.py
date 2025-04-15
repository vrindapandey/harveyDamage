import os
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io

# Load the trained model
model = load_model('models/bst_model.keras')  # Use the .keras format if you've saved your model that way

# Initialize the Flask app
app = Flask(__name__)

# Endpoint to get model summary
@app.route('/summary', methods=['GET'])
def model_summary():
    # Get model summary and return it as JSON
    model_info = []
    model.summary(print_fn=lambda x: model_info.append(x))
    return jsonify({'model_summary': model_info})

# Endpoint for image classification
@app.route('/inference', methods=['POST'])
def inference():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        
        # # Open image and preprocess it
        # img = Image.open(io.BytesIO(file.read()))
        # img = img.resize((150, 150))  # Resize to match the model input shape
        # img = tf.keras.preprocessing.image.img_to_array(img)
        # img = tf.expand_dims(img, axis=0)  # Add batch dimension

    
        # img_array = tf.expand_dims(img_array, axis=0)  # Shape: (1, 128, 128, 3)Image.open(file)

        img = Image.open(file).resize((128, 128))
        img_array = np.array(img) / 255.0
        img_list = np.expand_dims(img_array, axis=0) #.tolist()

        # Make prediction
        prediction = model.predict(img_list)
        predicted_class = 'damage' if prediction[0][0] < 0.5 else 'no_damage'  # Adjust threshold as needed

        # Return prediction in the required format
        return jsonify({'prediction': predicted_class})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
