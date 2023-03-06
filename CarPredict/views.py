from django.shortcuts import render
from joblib import load
model = load('./savedModels/model.joblib')

def predictor(request):
    return render(request,"main.html")

def formInfo(request):
    Year=int(request.GET.get("Year"))
    Present_Price=int(request.GET.get("Present_Price"))
    Kms_Driven=int(request.GET.get("Kms_Driven"))
    Seller_Type=int(request.GET.get("Seller_Type"))
    Fuel_Type=int(request.GET.get("Fuel_Type"))
    Transmission=int(request.GET.get("Transmission"))
    Owner=int(request.GET.get("Owner"))
    y_pred=model.predict([[Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]])
    
    return render(request,"result.html",{'result': int(y_pred*100000)})



 