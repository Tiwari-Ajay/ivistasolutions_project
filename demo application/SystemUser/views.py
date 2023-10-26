from django.shortcuts import render
from SystemUser.models import CandidateRegistration
import pymongo
import numpy as np
import json
import io
import pandas as pd
from collections import Counter
import socket
import sys
from PIL import Image
from bson.binary import Binary
import datetime #for temprary use for checkup need to remove
from django.http import HttpResponse
import subprocess #imported for adding tkinter file
# Create your views here.
def saveRegistration(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        name=first_name+" "+last_name
        email = request.POST.get("email")
        phone = request.POST.get("phone_number")
        profile = request.POST.get("usertype")
        address = request.POST.get("address")
        password = request.POST.get("password")
        temp_password = request.POST.get("temp_password")
        profile_image = request.FILES.get("profile_image")
        profile_image=profile_image.read()
        established_date=""
        if profile == "su":
            profile = "Sub_Admin"
        elif profile == "dt":
            profile = "Distiller"
            established_date = request.POST.get("established_number")
        elif profile == "dr":
            profile = "Distributor"
        elif profile == "rr":
            profile = "Retailor"
        if password == temp_password:
            client = pymongo.MongoClient("mongodb://localhost:27017")
            db = client["Track_and_Trace_data"]  # Replace with your database name
            #collection=db['retailor_details']
            #filter = {'email_id': email}
            #update = {'$set': {'photograph': profile_image}}
            #collection.update_one(filter, update)
            collection = db["new_registration"]
            data={'name':name,'email':email,'phone':phone,'profile':profile,'address':address,
                  'established_date':established_date,'profile_image':profile_image,'password':password}
            collection.insert_one(data)

            return render(request, "SystemUser/login.html")
        else:
            return render(request, "SystemUser/registration_new.html")

    return render(request, "SystemUser/registration_new.html")

def image_view(request,email_id):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['Track_and_Trace_data']
    collection1 = db['admin_details']
    collection2 = db["distiller_details"]
    collection3 = db["distributor_details"]
    collection4 = db["retailor_details"]
    #data=collection2.find_one({'email_id': email_id})['photograph']


    if (collection1.find_one({'email_id': email_id})!=None):
        return HttpResponse(collection1.find_one({'email_id': email_id})['photograph'], content_type='image/jpeg')

    elif (collection2.find_one({'email_id': email_id})!=None):
        return HttpResponse(collection2.find_one({'email_id': email_id})['photograph'], content_type='image/jpeg')

    elif (collection3.find_one({'email_id': email_id})!=None):
        return HttpResponse(collection3.find_one({'email_id': email_id})['photograph'], content_type='image/jpeg')

    elif (collection4.find_one({'email_id': email_id})!=None):
        return HttpResponse(collection4.find_one({'email_id': email_id})['photograph'], content_type='image/jpeg')

def userLogin(request):
    if request.method == 'POST':

        email=request.POST.get("email")
        password=request.POST.get("password")
        password = int(password)
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["Track_and_Trace_data"]  # Replace with your database name
        collection1 = db["admin_details"]
        collection2 = db["distiller_details"]
        collection3 = db["distributor_details"]
        collection4 = db["retailor_details"]
        if (collection1.find_one({'email_id': email,'password':password})!=None):
            return render(request, "SystemUser/index.html",context={'full_name': collection1.find_one({'email_id': email,'password':password})['admin_name'],'email_id':email})
        elif (collection2.find_one({'email_id': email, 'password': password})!=None):
            return render(request, "SystemUser/Distiller.html", context={'full_name': collection2.find_one({'email_id': email, 'password': password})['manufacturer_name'],'email_id':email})
        elif (collection3.find_one({'email_id': email, 'password': password})!=None):
            return render(request, "SystemUser/Distributor.html", context={'full_name': collection3.find_one({'email_id': email, 'password': password})['distributor_name'],'email_id':email})
        elif (collection4.find_one({'email_id': email, 'password': password})!=None):
            return render(request, "SystemUser/Retailor.html", context={'full_name': collection4.find_one({'email_id': email, 'password': password})['retailor_name'],'email_id':email})
    return render(request, "SystemUser/login.html")

#ADMIN VERIFY
def verifyRegistration(request):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["Track_and_Trace_data"]  # Replace with your database name
    collection = db["new_registration"]
    #data=collection.find({},{'established_date':0,'profile_image':0,'password':0})
    data = collection.find()
    print('this is the data')
    return render(request, "SystemUser/VerifyRegistration.html",context={"data":data})

def saveVerifiedRegistration(request,profile):
    '''
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["Track_and_Trace_data"]
    collection1 = db["new_registration"]
    collection2= db["new_registration"]'''
    print('hello')
    return render(request, "SystemUser/VerifyRegistration.html")
def deleteRegistration(request,email_id):
    '''
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["Track_and_Trace_data"]
    collection1 = db["new_registration"]
    collection2= db["new_registration"]'''
    print('hello')
    return render(request, "SystemUser/VerifyRegistration.html")
#to view admin
def datatable_admin_view_distiller(request):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["Track_and_Trace_data"]
    collection1 = db["distiller_to_distributor_details"]
    data=collection1.find().limit(2000)
    return render(request, "SystemUser/admin_view_distiller_data.html", context={'data':data})

def datatable_admin_view_distributor(request):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["Track_and_Trace_data"]
    collection1 = db["distributor_to_retailor_details"]
    data=collection1.find().limit(2000)
    return render(request, "SystemUser/admin_view_distributor_data.html", context={'data':data})

def datatable_admin_view_retailor(request):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["Track_and_Trace_data"]
    collection1 = db["retailor_to_outside_details"]
    data=collection1.find().limit(2000)
    return render(request, "SystemUser/admin_view_retailor_data.html", context={'data':data})
def available_stock(request):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["Track_and_Trace_data"]
    collection1 = db["distiller_to_distributor_details"]
    collection2 = db["distributor_to_retailor_details"]
    collection3 = db["retailor_to_outside_details"]
    data1 = collection1.find({'outstock_date': np.nan}).limit(1000)
    data2 = collection2.find({'outstock_date': np.nan}).limit(1000)
    data3 = collection3.find({'outstock_date': np.nan}).limit(1000)

    return render(request, "SystemUser/available_stock.html", context={'data1': data1,'data2': data2,'data3': data3})

def product_details(request):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["Track_and_Trace_data"]
    collection = db["distiller_to_distributor_details"]
    data = collection.find().limit(10000)
    return render(request, "SystemUser/product_details.html", context={'data': data})
def admin_distillerwise_analysis(request):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["Track_and_Trace_data"]
    collection = db["distiller_to_distributor_details"]
    data1=[]
    data2=[]
    data = collection.find().limit(10000)
    for x in data:
        data1.append(x['brand_name'])
        data2.append(x['product_quantity'])
    print(data2)
    keys_val=list(set(data1))
    count_val=[data1.count(x) for x in keys_val]
    keys_val1 = list(set(data2))
    count_val1 = [data2.count(x) for x in keys_val1]
    data1={"brand_name":keys_val,"count_val":count_val}
    data2 = {"product_quantity": keys_val1, "count_val": count_val1}
    print(data2)
    return render(request, "SystemUser/admin_distillerwise_analysis.html", context={'data1': json.dumps(data1),'data2': json.dumps(data2)})
#client server communication
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8080))
def server_page(request):
    """
    global server_socket
    server_socket.listen(5)
    while True:
        conn, addr = server_socket.accept()
        from_client = ''
        while True:
            data = conn.recv(4096)
            if (not data): break
            from_client += data.decode('utf8')
            print(from_client)
            # conn.send("received".encode())
        conn.close()
    print('client disconnected and shutdown')"""
    return render(request, "SystemUser/server_page.html")
def tkinter_server_run(request):
    subprocess.Popen(['python', 'SystemUser/unique_last_updated.py'])
    return render(request, "SystemUser/login.html")
def client_page(request):
    """
    print("Terminating the server...")
    global server_socket
    # Close the server socket
    server_socket.close()
    sys.exit(0)"""
    return render(request, "SystemUser/client_page.html")
def admin_report_generation(request):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["Track_and_Trace_data"]
    collection1 = db["distiller_to_distributor_details"]
    collection2 = db["distributor_to_retailor_details"]
    collection3 = db["retailor_to_outside_details"]
    data1 = collection1.find()
    data2 = collection2.find().limit(10000)
    data3 = collection3.find().limit(10000)
    distiller_data=[]
    data_frame=pd.DataFrame(data1)
    temp_data1=data_frame[data_frame['manufacture_name']=='John Distilleries Private Limited']
    temp_data2 = data_frame[data_frame['manufacture_name'] == 'Amrut Distilleries Pvt. Ltd.']
    '''
    a=dict(Counter(temp_data1['product_quantity']))[list(dict(Counter(temp_data1['product_quantity'])))[0]]
    b=dict(Counter(temp_data2['product_quantity']))[list(dict(Counter(temp_data2['product_quantity'])))[0]]
    c=dict(Counter(temp_data1['product_quantity']))[list(dict(Counter(temp_data1['product_quantity'])))[1]]
    d=dict(Counter(temp_data2['product_quantity']))[list(dict(Counter(temp_data2['product_quantity'])))[1]]
    '''
    a = list(dict(Counter(temp_data1['product_quantity'])).keys())[0]
    b = list(dict(Counter(temp_data2['product_quantity'])).keys())[0]
    c = list(dict(Counter(temp_data1['product_quantity'])).keys())[1]
    d = list(dict(Counter(temp_data2['product_quantity'])).keys())[1]
    a1 = dict(Counter(temp_data1['product_quantity']))[list(dict(Counter(temp_data2['product_quantity'])))[0]]
    b1 = dict(Counter(temp_data2['product_quantity']))[list(dict(Counter(temp_data2['product_quantity'])))[0]]
    c1 = dict(Counter(temp_data1['product_quantity']))[list(dict(Counter(temp_data2['product_quantity'])))[1]]
    d1 = dict(Counter(temp_data2['product_quantity']))[list(dict(Counter(temp_data2['product_quantity'])))[1]]
    if (a==b):
        if a==90:
            if (a1 > b1):
                distiller_data.append({"max_90": a1})
                distiller_data.append({"min_90": b1})
            else:
                distiller_data.append({"max_90": b1})
                distiller_data.append({"min_90": a1})
        else:
            if (c1 > d1):
                distiller_data.append({"max_180": c1})
                distiller_data.append({"min_180": d1})
            else:
                distiller_data.append({"max_180": d1})
                distiller_data.append({"min_180": c1})
    else:
        if (a==90):
            if (a1>d1):
                distiller_data.append({"max_90": a1})
                distiller_data.append({"min_90": d1})
            else:
                distiller_data.append({"max_90": d1})
                distiller_data.append({"min_90": a1})
            if (b1>c1):
                distiller_data.append({"max_180": b1})
                distiller_data.append({"min_180": c1})
            else:
                distiller_data.append({"max_180": c1})
                distiller_data.append({"min_180": b1})
        else:
            if (a1>d1):
                distiller_data.append({"max_180": a1})
                distiller_data.append({"min_180": d1})
            else:
                distiller_data.append({"max_180": d1})
                distiller_data.append({"min_180": a1})
            if (b1>c1):
                distiller_data.append({"max_90": b1})
                distiller_data.append({"min_90": c1})
            else:
                distiller_data.append({"max_90": c1})
                distiller_data.append({"min_90": b1})
    if len(temp_data1[temp_data1['product_quantity']==90])>len(temp_data2[temp_data2['product_quantity']==90]):
        distiller_data.append({"max_90_production_distiller": 'John Distilleries Private Limited'})
        distiller_data.append({"min_90_production_distiller": 'Amrut Distilleries Pvt. Ltd.'})
    else:
        distiller_data.append({"min_90_production_distiller": 'John Distilleries Private Limited'})
        distiller_data.append({"max_90_production_distiller": 'Amrut Distilleries Pvt. Ltd.'})
    if len(temp_data1[temp_data1['product_quantity']==180])>len(temp_data2[temp_data2['product_quantity']==180]):
        distiller_data.append({"max_180_production_distiller": 'John Distilleries Private Limited'})
        distiller_data.append({"min_180_production_distiller": 'Amrut Distilleries Pvt. Ltd.'})
    else:
        distiller_data.append({"min_180_production_distiller": 'John Distilleries Private Limited'})
        distiller_data.append({"max_180_production_distiller": 'Amrut Distilleries Pvt. Ltd.'})
    if len(temp_data1[temp_data1['product_quantity']==90])>len(temp_data2[temp_data2['product_quantity']==90]):
        distiller_data.append({"max_90_production_distiller": 'John Distilleries Private Limited'})
        distiller_data.append({"min_90_production_distiller": 'Amrut Distilleries Pvt. Ltd.'})
    else:
        distiller_data.append({"min_90_production_distiller": 'John Distilleries Private Limited'})
        distiller_data.append({"max_90_production_distiller": 'Amrut Distilleries Pvt. Ltd.'})
    test1=temp_data1[temp_data1['product_quantity']==90]
    print(len(test1[test1['outstock_date'].notnull()]))
    test2 = temp_data2[temp_data2['product_quantity'] == 90]
    print(len(test2[test2['outstock_date'].notnull()]))
    if (len(test1[test1['outstock_date'].notnull()])>len(test2[test2['outstock_date'].notnull()])):
        distiller_data.append({'max_90_export':len(test1[test1['outstock_date'].notnull()])})
        distiller_data.append({'min_90_export': len(test2[test2['outstock_date'].notnull()])})
        distiller_data.append({'distiller_with_max_90_export': 'John Distilleries Private Limited'})
        distiller_data.append({'distiller_with_min_90_export': 'Amrut Distilleries Pvt. Ltd.'})

    else:
        distiller_data.append({'min_90_export': len(test1[test1['outstock_date'].notnull()])})
        distiller_data.append({'max_90_export': len(test2[test2['outstock_date'].notnull()])})
        distiller_data.append({'distiller_with_min_90_export': 'John Distilleries Private Limited'})
        distiller_data.append({'distiller_with_max_90_export': 'Amrut Distilleries Pvt. Ltd.'})












    #print(a,b,c,d)
    '''
    if(a>b):
        distiller_data.append({"max_90":a})
        distiller_data.append({"min_90": b})
    else:
        distiller_data.append({"max_180": a})
        distiller_data.append({"min_180": b})
    if len(temp_data1)>len(temp_data2):
        distiller_data.append({"max_product_distiller": 'John Distilleries Private Limited'})
        distiller_data.append({"min_product_distiller": 'Amrut Distilleries Pvt. Ltd.'})
    else:
        distiller_data.append({"max_product_distiller": 'Amrut Distilleries Pvt. Ltd.'})
        distiller_data.append({"min_product_distiller": 'John Distilleries Private Limited'})
    '''


    return render(request, "SystemUser/admin_report_generation.html")

def map_admin_show_distiller(request):

    return render(request, "SystemUser/map_admin_show_distiller.html")
"""
def saveRegistration(request):
    if request.method == 'POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        phone=request.POST.get("phone_number")
        profile=request.POST.get("usertype")
        id_number=-1
        
        if profile == "su" or profile == "dt":
            reg_number=request.POST.get("reg_number")
            reg_date=request.POST.get("reg_date")
        else:
            id_number=request.POST.get("id_number",)
        
        address=request.POST.get("address")
        password=request.POST.get("password")
        temp_password=request.POST.get("temp_password")
        profile_image=request.FILES.get("profile_image")
        if profile == "su":
            profile="Sub_Admin"
        elif profile == "dt":
            profile="Distiller"
        elif profile == "dr":
            profile="Distributor"
        elif profile == "rr":
            profile="Retailor"
        if password == temp_password:

            if profile == "su" or profile == "dt":
                cr=CandidateRegistration(first_name=first_name,last_name=last_name,email=email,
                                     phone=phone,profile=profile,reg_number=reg_number,reg_date=reg_date,
                                     id_number=id_number,address=address,password=password,profile_image=profile_image)
                cr.save()
            else:
                cr = CandidateRegistration(first_name=first_name, last_name=last_name, email=email,
                                           phone=phone, profile=profile, reg_number="", reg_date=datetime.date(1997, 10, 19),
                                           id_number=id_number, address=address, password=password,profile_image=profile_image)
                cr.save()

            return render(request, "SystemUser/login.html")
        else:
            return render(request, "SystemUser/registration.html")

    return render(request, "SystemUser/registration_new.html")
"""

#for Registration by Distiller
def RegistrationByDistiller(request):
    if request.method == 'POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        phone=request.POST.get("phone_number")
        profile=request.POST.get("usertype")
        id_number=-1
        if profile == "su" or profile == "dt":
            reg_number=request.POST.get("reg_number")
            reg_date=request.POST.get("reg_date")
        else:
            id_number=request.POST.get("id_number",)
        address=request.POST.get("address")
        password=request.POST.get("password")
        temp_password=request.POST.get("temp_password")
        profile_image=request.FILES.get("profile_image")
        if profile == "su":
            profile="Sub_Admin"
        elif profile == "dt":
            profile="Distiller"
        elif profile == "dr":
            profile="Distributor"
        elif profile == "rr":
            profile="Retailor"
        if password == temp_password:
            
            if profile == "su" or profile == "dt":
                cr=CandidateRegistration(first_name=first_name,last_name=last_name,email=email,
                                     phone=phone,profile=profile,reg_number=reg_number,reg_date=reg_date,
                                     id_number=id_number,address=address,password=password,profile_image=profile_image)
                cr.save()
            else:
                cr = CandidateRegistration(first_name=first_name, last_name=last_name, email=email,
                                           phone=phone, profile=profile, reg_number="", reg_date=datetime.date(1997, 10, 19),
                                           id_number=id_number, address=address, password=password,profile_image=profile_image)
                cr.save()
            
            return render(request, "SystemUser/login.html")
        else:
            return render(request, "SystemUser/RegistrationByDistiller.html")
    return render(request, "SystemUser/RegistrationByDistiller.html")
#for Registration by Distributor
def RegistrationByDistributor(request):
    if request.method == 'POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        phone=request.POST.get("phone_number")
        profile=request.POST.get("usertype")
        id_number=-1
        if profile == "su" or profile == "dt":
            reg_number=request.POST.get("reg_number")
            reg_date=request.POST.get("reg_date")
        else:
            id_number=request.POST.get("id_number",)
        address=request.POST.get("address")
        password=request.POST.get("password")
        temp_password=request.POST.get("temp_password")
        profile_image=request.FILES.get("profile_image")
        if profile == "su":
            profile="Sub_Admin"
        elif profile == "dt":
            profile="Distiller"
        elif profile == "dr":
            profile="Distributor"
        elif profile == "rr":
            profile="Retailor"
        if password == temp_password:
            
            if profile == "su" or profile == "dt":
                cr=CandidateRegistration(first_name=first_name,last_name=last_name,email=email,
                                     phone=phone,profile=profile,reg_number=reg_number,reg_date=reg_date,
                                     id_number=id_number,address=address,password=password,profile_image=profile_image)
                cr.save()
            else:
                cr = CandidateRegistration(first_name=first_name, last_name=last_name, email=email,
                                           phone=phone, profile=profile, reg_number="", reg_date=datetime.date(1997, 10, 19),
                                           id_number=id_number, address=address, password=password,profile_image=profile_image)
                cr.save()
                
            return render(request, "SystemUser/login.html")
        else:
            return render(request, "SystemUser/RegistrationByDistributor.html")
    return render(request, "SystemUser/RegistrationByDistributor.html")

def verify_Registration(request):
    #candidate_data=CandidateRegistration.objects.all()[0]
    #first_name=candidate_data.first_name
    return render(request, "SystemUser/VerifyRegistration.html")

def userManagementAdminDistiller(request):
    return render(request, "SystemUser/UserManagement_Admin_Distiller.html")

def userManagementDistributorRetailor(request):
    return render(request, "SystemUser/UserManagement_Distributor_Retailor.html")

def dataLoading(request):
    return render(request, "SystemUser/DataLoading.html")

"""
#for check login
def userLogin(request):
    if request.method == 'POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        datasets=CandidateRegistration.objects.all()
        full_name=""
        profile=""
        user_status=False
        for data in datasets:
            if data.email == email and data.password == password:
                user_status=True
                full_name = data.first_name+' '+data.last_name
                profile=data.profile
                profile_image=data.profile_image
                break
        if user_status == True:
            profile=profile.lower()
            if profile == 'admin' or profile == 'sub_admin':
                return render(request, "SystemUser/index.html",context={'full_name':full_name,'profile_image':profile_image})
            elif profile == 'distiller':
                return render(request, "SystemUser/Distiller.html",context={'full_name':full_name})
            elif profile == 'distributor':
                return render(request, "SystemUser/Distributor.html",context={'full_name':full_name})
            else:
                return render(request, "SystemUser/Retailor.html",context={'full_name':full_name})
        else:
            return render(request, "SystemUser/login.html")

    return render(request, "SystemUser/login.html")

"""
#distillerwise analysis
def distillerwise_analysis(request):
    return render(request, "SystemUser/distillerwise_analysis.html")
def superuser(request):
    return render(request, "SystemUser/SuperUser.html")

#new added
def index(request):
    return render(request, "SystemUser/index.html")

def distiller(request):
    return render(request, "SystemUser/Distiller.html")

def distributor(request):
    return render(request, "SystemUser/Distributor.html")

def retailor(request):
    return render(request, "SystemUser/Retailor.html")




