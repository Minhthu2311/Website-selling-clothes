from django.shortcuts import render
from django.forms import modelform_factory, widgets
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'registration/register.html', {'form': form})
@login_required
def profile(req):
    UserEditForm = modelform_factory(
        get_user_model(), fields=('first_name', 'last_name', 'username'))
    form = UserEditForm(instance=req.user)
    if req.method == "POST":
        form = UserEditForm(instance=req.user, data=req.POST)
        if form.is_valid():
            form.save()
    return render(req, 'registration/profile.html', {'form': form})
