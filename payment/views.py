from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.response import Response
import datetime
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
import json

# Create your views here.

@api_view(['GET', 'POST'])
@login_required(login_url='login')
def pay(request):
    # return Response({'success':True})
    if request.method != 'POST':
        return render(request, 'payment.html', {'success':True})