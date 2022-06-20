from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
  
# Create your views here.
def hotel_image_view(request):
  
    if request.method == 'POST':
      name = request.POST["name"]
      files = request.FILES
      image = files.get("image")

      i = Image.open(image)
      thumb_io = BytesIO()
      i.save(thumb_io, format='JPEG', quality=80)
      inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, 'foo.jpeg', 'image/jpeg', thumb_io.tell(), None)
      hotel = Hotel(name=name, hotel_Main_Img=inmemory_uploaded_file)
      hotel.save()
      return redirect('success')      
    else:
      form = HotelForm()
      return render(request, 'image_app/hotel_image_form.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')


def display_hotel_images(request):
  
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all() 
        return render(request, 'image_app/display_hotel_images.html',
                     {'hotel_images' : Hotels})