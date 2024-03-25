import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os
import numpy as np
import tflite
from PIL import Image

def detect(folder, filename):
    path = os.path.join('uploads', folder, filename)

    TF_MODEL_FILE_PATH = 'helpers/model_detection/model_4_Data_300.tflite' # The default path to the saved TensorFlow Lite model
    class_names = open('helpers/model_detection/class_names.txt', "r").read().split('\n')
    interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)
    # return interpreter.get_signature_list()
    classify_lite = interpreter.get_signature_runner('serving_default')

    # with open(TF_MODEL_FILE_PATH, 'rb') as f:
    #     buf = f.read()
    #     model = tflite.Model.GetRootAsModel(buf, 0)

    img = tf.keras.utils.load_img(
        path, target_size=(160,160) 
    )

    img_rescale = layers.Rescaling(1./255)(img)
    img_array = tf.keras.utils.img_to_array(img_rescale)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = classify_lite(args_0 = img_array)['dense_1']
    score = tf.nn.softmax(predictions)

    return class_names[np.argmax(score)], 100 * np.max(score)
