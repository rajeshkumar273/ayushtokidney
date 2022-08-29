from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pickle
import datetime
# Create your views here.
def AtoK(request):
    return render(request,'AtoK_app/AtoK.html')
def home(request):
    return render(request,'AtoK_app/home.html')
def aboutus(request):
    return render(request,'AtoK_app/aboutus.html')
def expertSystem(request):
    return render(request,'AtoK_app/chatbot.html')
def predict(request):
    return render(request,'AtoK_app/predict.html')
def result(request):
    model = pickle.load(open('Kidney.pkl', 'rb'))
    sg = float(request.GET['sg'])
    htn = float(request.GET['htn'])
    hemo = float(request.GET['hemo'])
    dm = float(request.GET['dm'])
    al = float(request.GET['al'])
    appet = float(request.GET['appet'])
    rc = float(request.GET['rc'])
    pc = float(request.GET['pc'])

    values = np.array([[sg, htn, hemo, dm, al, appet, rc, pc]])
    pred = model.predict(values)

    return render(request,'AtoK_app/result.html',{'prediction':str(pred)})
   


    
