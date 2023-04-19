from django.shortcuts import render
from . forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import Alzhimer
from . Alzhimerserializer import alzhimerSerializers
from tensorflow import keras
# import joblib
from keras.models import load_model
# from tensorflow.keras.models import load_model
import keras
from keras import layers

from matplotlib import pyplot as plt
import pandas as pd
# %matplotlib inline
import numpy as np
import os
import cv2 as ocv
# import pickle
# import threading
from rest_framework.views import APIView
# import tempfile
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def approveBrain(request):
    
    if request.method == 'POST':
        model_path = os.path.join(os.path.dirname(__file__), 'model', 'Brain Tumor detection.h5')
        model = load_model(model_path)
        image_file = request.FILES['image']
        # return JsonResponse({'image':"2"})
        image = ocv.imdecode(np.frombuffer(image_file.read(), np.uint8), ocv.IMREAD_UNCHANGED)

        # return JsonResponse({'image':"3"})
    
        # Preprocess the image
        # image = preprocess_image(image)
        SIZE = 64
        image = ocv.resize(image, (SIZE, SIZE))
        image = ocv.cvtColor(image, ocv.COLOR_RGB2BGR)
        image = image / 255
        image = np.expand_dims(image, axis=0)


        predictions = model.predict(image)
    
        # Make a prediction with the loaded model
        # prediction = model.predict(image)
        # Convert the prediction to a JSON string
        # prediction_json = json.dumps(prediction.tolist())
        
        prediction = np.argmax(model.predict(image)) 

        # return JsonResponse({'2':prediction})

        if int(prediction) == 0:
            return JsonResponse({'type':'glioma'})
        elif int(prediction) == 1:
            # print('meningioma')
            return JsonResponse({'type':'meningioma'})

        elif int(prediction) == 2:
            # print('notumor')
           return JsonResponse({'type':'notumor'})
        else :
           return JsonResponse({'type':'pituitary'})

    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def approveAlzhimer(request):
      if request.method == 'POST':
        model_path = os.path.join(os.path.dirname(__file__), 'model', 'zheimer.h5')
        model = load_model(model_path)
        image_file = request.FILES['image']
        # return JsonResponse({'image':"2"})
        image = ocv.imdecode(np.frombuffer(image_file.read(), np.uint8), ocv.IMREAD_UNCHANGED)

        # return JsonResponse({'image':"3"})
    
        # Preprocess the image
        image = preprocess_image(image)

        # predictions = model.predict(image)
    
        # Make a prediction with the loaded model
        # prediction = model.predict(image)
        # Convert the prediction to a JSON string
        # prediction_json = json.dumps(prediction.tolist())        
        # Pass the preprocessed image through the model
        # Get the predicted class label
        prediction = np.argmax(model.predict(image)) 

        if prediction == 0:
            # print('MildDemented')
            return JsonResponse({'type':'MildDemented'})
        elif prediction == 1:
            return JsonResponse({'type':'ModerateDemented'})

        elif prediction == 2:
            return JsonResponse({'type':'NonDemented'})
        else :
            return JsonResponse({'type':'VeryMildDemented'})
            
        # #prediction = le.inverse_transform([prediction])  #Reverse the label encoder to original name
        # print("The prediction for this image is: ", prediction)
        # #print("The actual label for this image is: ", prediction[0]) 

def preprocess_image(image):
    # Preprocess the image here (e.g. resize, normalize, etc.)
    # image = ocv.resize(image,(100,100))
    # img = (np.array(img).flatten())/255
    SIZE = 100
    image = ocv.resize(image, (SIZE, SIZE))
    image = ocv.cvtColor(image, ocv.COLOR_RGB2BGR)
    image = image / 255
    image = np.expand_dims(image, axis=0)

    return image