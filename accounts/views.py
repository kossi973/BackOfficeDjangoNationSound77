from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import redirect, render
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from .forms import UserProfileForm
from .models import UserProfile
import re

User = get_user_model()

def user_info(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('Home Page')  # Redirige vers la page d'accueil
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'accounts/user_info.html', {'form': form})

# def user_info(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST)
#         if form.is_valid():
#             user_profile, created = UserProfile.objects.get_or_create(user=request.user)
#             user_profile.first_name = form.cleaned_data['first_name']
#             user_profile.last_name = form.cleaned_data['last_name']
#             user_profile.address = form.cleaned_data['address']
#             user_profile.email = form.cleaned_data['email']
#             user_profile.save()
#             return redirect('Home Page')
#     else:
#         form = UserProfileForm()
#     return render(request, 'accounts/user_info.html', {'form': form})


#Requête d'inscription
def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            if not username or not password: 
                messages.error(request, 'Nom d\'utilisateur et mot de passe sont requis.') 
                return render(request, 'accounts/signup.html')
            
            if len(username) < 6:
                messages.error(request, 'Le nom d\'utilisateur doit contenir au moins 6 caractères.') 
                return render(request, 'accounts/signup.html')
            
            #Vérifier unicité du nom
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Ce nom d\'utilisateur est déjà pris.')
                return render(request, 'accounts/signup.html')
            
            if len(password) < 10:
                messages.error(request, 'Le mot de passe doit contenir au moins 10 caractères.') 
                return render(request, 'accounts/signup.html')
            
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                messages.error(request, 'Le mot de passe doit contenir au moins un caractère spécial.')
                return render(request, 'accounts/signup.html')
                
            user = User.objects.create_user(username=username, password=password)

            if user:
                login(request, user)
                return redirect('Home Page')
            else:
                messages.error(request, 'Une erreur est survenue lors de la création du compte.')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = RegistrationForm()    
    return render(request, 'accounts/signup.html', {'form': form})


#Requête de connexion
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            #Connecter l'utilisateur
            login(request, user)
            return redirect('Home Page')
        else:
            # messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def organisateur(request):
    est_organisateur = request.user.groups.filter(name='Organisateur').exists()
    return render(request, 'accounts/login.html', {'est_organisateur': est_organisateur})


#Requête de déconnexion
def logout_user(request):
    logout(request)    
    return redirect('Home Page')

