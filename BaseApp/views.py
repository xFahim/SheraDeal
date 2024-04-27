from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Avg

# Create your views here.

@login_required(login_url='login_view')
def home(request):
    return render(request, 'home.html')

# radiah
def CreateNewAcc(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create user
        """
            ------ Manual SQL Command to simulate such----------
            INSERT INTO auth_user (username, email, password, is_superuser, is_staff, is_active, date_joined)
            VALUES ('Fahim', 'test@example.com', 'hashed_password', FALSE, FALSE, TRUE, NOW());

            here, django automatically hashes the password,
            to do it manually we can use the following, (ref django.contrib.auth.hashers)

            password = make_password('plain_text_password')

        """
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            # Login the user
            login(request, user)
            # Redirect to home page.
            return redirect('home')
        except IntegrityError:
            messages.error(request, 'Username is already taken.')
        
        
    return render(request, 'signup.html')

# mustafiz
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        """
        ----- Manual SQL Command to simulate such------
        
        SELECT * FROM auth_user
        WHERE username = 'input-username' AND password = 'input-hashed_password';

        -------- This query will return None if it doesn't match any record of users ------ 
        -------- Otherwise we can authenticate the user ---------------- 

        -------- we can hash the password using django hash func -----


        """

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to home.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')

def dashboard(request):
    return render(request, 'dashboard.html')

def add_to_wishlist(request):
    return render(request, 'home.html')

# mahbub
def search_view(request):
    skey = request.GET.get('searchKey')

    searchType = request.GET.get('searchType')
    location_txt = request.GET.get('location')

    # Get search results
    results = Gadget_Data.objects.filter(name__icontains=skey)
    """

    ----     Manual SQL Command   ---

    SELECT * 
    FROM BaseApp_gadget_data 
    WHERE UPPER(name) LIKE UPPER('%skey%');

    """

    # list of dict to store feedback along side each gadgetData
    gadget_data_feedbacks = []
    # fetch feedbacks
    for result in results:
        feedbacks = Feedback.objects.filter(Gadget_id=result)
        website_source = result.SourceID

        # Calculate average rating
        avg_rating = feedbacks.aggregate(Avg('rating'))['rating__avg']

        '''
        ------- Manual SQL -----
        SELECT AVG(rating)
        FROM Feedback 
        WHERE Gadget_id = result;
        '''

        if avg_rating == None:
            avg_rating = 0
        else:
            avg_rating = round(avg_rating, 2)

        # Store gadget data and feedbacks
        gadget_data_feedbacks.append({'gadget_data': result, 'feedbacks': feedbacks, 'avg_rating': avg_rating, 'website_source': website_source})

    if searchType == "rating":
        gadget_data_feedbacks.sort(key=lambda x: x['avg_rating'], reverse=True)
    else:
        gadget_data_feedbacks.sort(key=lambda x: x['gadget_data'].price)

    return render(request, 'SearchRes.html', {'gadget_data_feedbacks': gadget_data_feedbacks, 'searchKey':skey})

def detail_view(request):
    return redirect('home')

def error_page(request):
    return render(request,'error_page.html')

def add_feedback(request):
    if request.method == 'POST':
        gadget_id = request.POST.get('gadget_id')
        skey = request.POST.get('skey')
        feedback_text = request.POST.get('feedback')
        rating = request.POST.get('rating')
        user = request.user
        

        # Save the feedback to the database
        feedback = Feedback.objects.create(
            Gadget_id_id=gadget_id,
            user=user,
            Feedback=feedback_text,
            rating=rating
        )

        return redirect('home')

    # If the request method is not POST, its invalid request
    return redirect('error_page')  #