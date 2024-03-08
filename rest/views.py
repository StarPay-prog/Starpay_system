from django.shortcuts import render
import json

import requests
from dashboard.models import *
from django.http import JsonResponse
from starpay.settings import base_url,payout_url
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
def merchant_status(request):
    if request.method == "POST":
        try:
            # Retrieve JSON data from request body
            data = json.loads(request.body)
            user = data.get('user')
            service = data.get('ser')
            print(service,type(service))
            print(user)  # This should print 'aditya' if 'data' contains the value 'aditya'
            url = base_url + 'update-merchant-admin/'+user
            jwt_token = request.session.get('jwt_token_access')
            header = {
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json"  # Assuming you are sending JSON data
            }
            data2={
                "data":{
                "service_option": service
                }
            }
            data2 = json.dumps(data2)
            print(data2)
            response = requests.patch(url,data = data2, headers=header,)
            data = response.json()
            print(data)
            # Process the user data as needed
            
            # Return a JSON response
            return JsonResponse({'message': 'Success'})
        except json.JSONDecodeError:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)     


def merchant_ip(request):
    if request.method == "POST":
        try:
            # Retrieve JSON data from request body
            data = json.loads(request.body)
            user = data.get('user')
            ip = data.get('ser')
            print("data",user,ip)  # This should print 'aditya' if 'data' contains the value 'aditya'
            url = payout_url+'Rest/payout-update-merchant-admin/'+user
            jwt_token = request.session.get('jwt_token_access')
            header = {
                "Access": jwt_token,
                "Content-Type": "application/json"  # Assuming you are sending JSON data
                }
            data2 ={
                "ip_addres": ip
            }
            response1 = requests.patch(url, headers=header,data = json.dumps(data2))
            # Process the user data as needed
            
            # Return a JSON response
            return JsonResponse({'message': 'Success'})
        except json.JSONDecodeError:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def virtual_transaction(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        userdata=request.session.get('user_data')
       
        if data.get('method') == '1':
            json_data ={
                        "Debit": "starpay_account",
                        "Credit": "papasy3988",
                        "Transaction_amount": data.get('amount'),
                        "Transaction_remark": (data.get('remarks') or ' ') + 'Wallet of merchant credited by ' + userdata['data']['emp_id']
                    }
            
        elif data.get('method') == '2':
            json_data ={
                        "Debit": "papasy3988",
                        "Credit": "starpay_account",
                        "Transaction_amount": data.get('amount'),
                        "Transaction_remark": (data.get('remarks') or ' ') + 'Wallet of merchant Debited by ' + userdata['data']['emp_id']
                    }
        else:
            return JsonResponse("Not working")
        
        url = payout_url + "Rest/payout-wallet-transaction/"
        header = {
        "Access": request.session['jwt_token_access'],
        "Content-Type": "application/json"  # Assuming you are sending JSON data
        }
          
        response = requests.post(url, data=json.dumps(json_data),headers=header)   
        if response.status_code == 200 :
            response_data = response.json()
            return JsonResponse(response_data) 
        else:
            return JsonResponse({"message":"Transaction Failed"})



def update_callbackurl(request):

    if request.method == 'POST':
        try:
            # Retrieve JSON data from request body
            data = json.loads(request.body)
            user = data.get('user')
            url = data.get('ser')
            print("data",user,url)  # This should print 'aditya' if 'data' contains the value 'aditya'
            url = payout_url+'Rest/payout-update-merchant-admin/'+user
            jwt_token = request.session.get('jwt_token_access')
            header = {
                "Access": jwt_token,
                "Content-Type": "application/json"  # Assuming you are sending JSON data
                }
            data2 ={
                "webhook_url":url

            }
            response1 = requests.patch(url, headers=header,data = json.dumps(data2))
            # Process the user data as needed
            
            # Return a JSON response
            return JsonResponse({'message': 'Success'})
        except json.JSONDecodeError:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
        
