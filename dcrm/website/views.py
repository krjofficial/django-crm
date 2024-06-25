from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record 
from .forms import AddRecordForm


# Create your views here.
def home(request):

  records = Record.objects.all()

  # Check to see if logging in 
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    # Check to see if user is valid (Authentication)
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('home')
    else:
      messages.error(request, 'Invalid username or password')
      return redirect('home')
  else:
    return render(request, 'home.html', {'records': records})



def logout_user(request):
  logout(request)
  messages.success(request, 'You are now logged out')
  return redirect('home')

def user_record(request, pk):
  #check if the user is logged in 
  if request.user.is_authenticated:
    #look up record
    user_record = Record.objects.get(id=pk)
    return render(request, 'record.html', {'user_record': user_record})
  else:
    messages.success(request, "Please login to View this record")
    return redirect('home')
  

def delete_record(request, pk):
  if request.user.is_authenticated:
    delete_it = Record.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "Record deleted")
    return redirect('home')
  else:
    messages.success(request, "Login to Delete Records")
    return redirect('home')
  


def add_record(request):
  form = AddRecordForm(request.POST or None)
  if request.user.is_authenticated:
    if request.method == "POST":
      if form.is_valid():
        form.save()
        messages.success(request, "Record Added")
        return redirect('home')
    return render(request, 'add_record.html', {'form': form})
  else:
    messages.success(request, "Login to Add Records")
    return redirect('home')

  