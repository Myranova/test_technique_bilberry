from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import PhotoForm
from .models import Photo
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'main_app/base.html')

def contact_photo(request):
    sauvegarde = False
    form = PhotoForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Photo()
        contact.nom = form.cleaned_data['nom']
        contact.photo = form.cleaned_data['photo']
        contact.timestamp = "0012"
        contact.rejected_flag = False
        contact.verified_flag = False
        contact.save()
        sauvegarde = True
    else:
        print("form is not valid") 

    return render(request, 'main_app/contact_photo.html', {
        'form' : form,
        'sauvegarde' : sauvegarde
    })

def image_list(request):
    return render(request, 'main_app/image_list.html', {'photos' : Photo.objects.all()})    

def image_viewer(request, id_photo, choice_flag):
    if int(id_photo) > Photo.objects.all().count() :
        return render(request, 'main_app/error.html')
    if int(id_photo) > 0 and int(id_photo) < 6 :
        if choice_flag == '0':
            photo = Photo.objects.get(id=id_photo)
            photo.verified_flag = True
            photo.rejected_flag = True
            photo.save()
        if choice_flag == '1':
            photo = Photo.objects.get(id=id_photo)
            photo.verified_flag = True
            photo.rejected_flag = False
            photo.save()
        return render(request, 'main_app/image_viewer.html', {'photo' : Photo.objects.get(id=int(id_photo)), 'id_next' : int(id_photo) + 1})
    return render(request, 'main_app/base.html') 

