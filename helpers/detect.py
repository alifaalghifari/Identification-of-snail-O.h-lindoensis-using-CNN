# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# import keras
import os
import numpy as np
from PIL import Image
# import tflite
import tflite_runtime.interpreter as tflite

# def detect(folder, filename):
#     path = os.path.join('uploads', folder, filename)

#     TF_MODEL_FILE_PATH = 'helpers/model_detection/model_4_Data_300.tflite' # The default path to the saved TensorFlow Lite model
#     class_names = open('helpers/model_detection/class_names.txt', "r").read().split('\n')
    
#     interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)
#     # return interpreter.get_signature_list()
#     classify_lite = interpreter.get_signature_runner('serving_default')

#     # with open(TF_MODEL_FILE_PATH, 'rb') as f:
#     #     buf = f.read()
#     #     model = tflite.Model.GetRootAsModel(buf, 0)

#     img = tf.keras.utils.load_img(
#         path, target_size=(160,160) 
#     )

#     img_rescale = layers.Rescaling(1./255)(img)
#     img_array = tf.keras.utils.img_to_array(img_rescale)
#     img_array = tf.expand_dims(img_array, 0) # Create a batch

#     predictions = classify_lite(args_0 = img_array)['dense_1']
#     score = tf.nn.softmax(predictions)

#     return class_names[np.argmax(score)], 100 * np.max(score)

def softmax(x):
    # Compute softmax values for each element of the input array
    exp_x = np.exp(x - np.max(x))  # Subtract the maximum value to avoid overflow
    return exp_x / np.sum(exp_x)

def detect_lite(folder, filename):
    path = os.path.join('uploads', folder, filename)
    print('masuk')
    # return 'tes', 30
    try:
        TF_MODEL_FILE_PATH = 'helpers/model_detection/model_4_Data_300.tflite' # The default path to the saved TensorFlow Lite model
        class_names = open('helpers/model_detection/class_names.txt', "r").read().split('\n')
        
        TARGET_SIZE = (160, 160)

        with open(TF_MODEL_FILE_PATH, 'rb') as fid:
            tflite_model = fid.read()
            
        # return 'tes', 30
        
        interpreter = tflite.Interpreter(model_content=tflite_model)
        
        # return 'tes', 30
        interpreter.allocate_tensors()
        
        # Prepare input data (example: a single image)
        img = Image.open(path)  

        resize_img = img.resize(TARGET_SIZE)

        arr_img = np.float32(resize_img)

        rescaled_img = arr_img / 255.0



        arr_expand = np.expand_dims(rescaled_img, 0)

        # Set input tensor
        input_index = interpreter.get_input_details()[0]['index']
        # print(interpreter.get_input_details()[0])
        # print(arr_expand.shape)
        interpreter.set_tensor(input_index, arr_expand)

        # # Run inference
        interpreter.invoke()

        # Get output tensor
        output_index = interpreter.get_output_details()[0]['index']
        output_data = interpreter.get_tensor(output_index)

        softmax_result = softmax(output_data[0])

        return ({'class name' : class_names[np.argmax(softmax_result)], 'score': 100 * np.max(softmax_result)})
    
    except Exception as e:
        print(e)
        return ({'message': 'error', 'data' : e})
    