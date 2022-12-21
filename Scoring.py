import os
import json
from PIL import Image
import tensorflow as tf
from azureml.contrib.services.aml_request import rawhttp
from azureml.contrib.services.aml_response import AMLResponse

def init():
    global model
    model = tf.keras.models.load_model(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "final_model.h5"))

@rawhttp
def run(request):
    if request.method != 'POST':
        return AMLResponse(f"Unsupported verb: {request.method}", 400)
    image_data = request.files['image']
    img = Image.open(image_data)
    img = img.resize((224,224)).convert('RGB')
    img = tf.keras.utils.img_to_array(img)
    img = img.reshape(1,224,224,3)
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    result = model.predict(img)
    if result[0] == 1:
        return AMLResponse(json.dumps({"Result": "It's a dog!"}), 200)
    else:
        return AMLResponse(json.dumps({"Result": "It's not a dog!"}), 200)