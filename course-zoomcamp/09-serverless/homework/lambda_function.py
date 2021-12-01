import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor


preprocessor = create_preprocessor('xception', target_size=(150, 150))


interpreter = tflite.Interpreter(model_path='cats-dogs-v2.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

def predict(url):
    input = preprocessor.from_url(url)
    interpreter.set_tensor(input_index, input)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_index)[0][0]

    return dict({'prediction': str(predictions)})

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result