from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if(request.method == "POST"):
        contact_form = ContactForm(data=request.POST)
        if(contact_form.is_valid()):#Valida si todos los campos estan rellanados correctamente en el formulario
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
            "La Caffettiera: Nuevo mensaje de contacto",#Asunto
            "De {} <{}> \n\nEscribió:\n\n{}".format(name,email,content),#Cuerpo
            "no-contestar@inbox.mailtrap.io",#Email de Origen
            ["jaimeandres708@hotmail.com"],#Otros Email de Destino
            reply_to = [email]  #Correo de la persona que lleno el formulario
            )

            try:
                email.send()#Método para enviar el correo
                #Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact') + "?ok")
            except:
                #Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact') +"?fail")

    return render(request,"contact/contact.html", {'form':contact_form})
