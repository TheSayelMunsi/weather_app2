from multiprocessing import context
import requests
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import City
from .forms import cityform
# Create your views here.
def index(request):
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f6db9770496ae7a494e2ada6fb5f1a31'    
    error=''
    message=''
    message_class=''
    cities=City.objects.all()
    weather_list=[]
    if request.method=='POST':
        form=cityform(request.POST)
        if form.is_valid():
            new_city=form.cleaned_data['name']
            existing_city=City.objects.filter(name=new_city).count()

            if existing_city == 0:
                r=requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    error= 'City does not exist in the world'
            else:
                error = "City already exists"
        if error:
            message= error
            message_class='alert-danger'
        else:
            message = 'city added successfully'
            message_class= 'alert-success '
    form=cityform()
    for city in cities:
        r=requests.get(url.format(city)).json()
        #print(r.text)
           

        weathers={
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_list.insert(0,weathers)
    
    
    context={
        'weather_list': weather_list,
        'form':form,
        'message': message,
        'message_class': message_class
    }
    
   
    return render(request,'weather.html',context)

def delete(request,city_name):
    City.objects.get(name=city_name).delete()

    return redirect('home')
