from django.shortcuts import render, redirect

#메일용 모듈
from django.views.generic import View

def main(request):
    return render(request, 'index.html')

# #contact
# def contact_form(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             return redirect(('concact:complete'))