from django.shortcuts import render
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            print(f"Name: {name}, Email: {email}, Message: {message}")
            return render(request, 'myapp/success.html', {'name': name})

    return render(request, 'myapp/contact.html', {'form': form})


