from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer

# Create your views here.


# @api_view(['GET', 'POST'])
def login(request):

    if request.user and request.user.is_authenticated:
        return redirect('index')
    
    if request.method != 'POST':
        return render(request, 'login.html')
    elif request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            django_login(request, user)
            return redirect('index')
        
        return render(request, 'login.html', context={'invalid' : True})


@api_view(['GET', 'POST'])
def register(request):
    if request.user and request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()
            # login(request, user)

            return Response({'success':True}, status=200)
        
        return Response(serializer.errors, status=400)
        # data = request.POST
        # if 'name' not in data:
        #     response['field'] = 'name'
        # elif 'username' not in data:
        #     response['field'] = 'username'
        # elif 'password' not in data:
        #     response['field'] = 'password'

        # return JsonResponse(response, safe=False)
        
def logout(request):

    django_logout(request)

    return redirect('login')

@api_view(['GET', 'POST'])
def payment(request):
    # if request.user and request.user.is_authenticated:
    #     return redirect('payment')
    # if request.method == 'GET':
    #     pass
    # elif request.method == 'POST':
    #     pass

    return render(request, '../payment/templates/payment.html', context={'success': True})
