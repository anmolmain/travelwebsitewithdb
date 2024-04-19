from django.shortcuts import redirect, render
from eventhorizon.models import Trip, SendToTrip
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth, User




def home(request):
    return render(request, 'home.html')

def login(request):
    try:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                messages.info(request, "Invalid Credential")
                return redirect("login")
        else:
            return render(request, "login.html")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("login")

# Register view to register user
def register(request):
    try:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            email = request.POST["email"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already exist")
                    return redirect("register")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email already registered")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password1,
                    )
                    user.save()
                    return redirect("login")
            else:
                messages.info(request, "Password not matches")
                return redirect("register")
        else:
            return render(request, "register.html")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("register")

# Logout view to logout user
def logout(request):
    try:
        auth.logout(request)
        return redirect("/")
    except Exception as e:
        messages.error(request, str(e))
        return redirect("/")

def checkout(request):
    return render(request, 'checkout.html')

def contactUs(request):
    return render(request, 'contactUs.html')

def trips(request):
    trips = Trip.objects.all()
    tripsD = {"trips": trips}
    return render(request, 'trips.html', tripsD)

def save_booking(request):
    if request.method == 'POST':
        destination = request.POST['destination']
        name = request.POST['name']
        date = request.POST['date']
        time = request.POST['time']
        boarding = request.POST['boarding']
        contactm = request.POST['contactm']
        contacte = request.POST['contacte']

        # Save to SendToTrip model
        send_to_trip = SendToTrip(
            destination=destination,
            name=name,
            date=date,
            time=time,
            boarding=boarding,
            contactm=contactm,
            contacte=contacte
        )
        send_to_trip.save()

        # Optionally, save to Trip model if you want to save it there as well
        # Here I'm just showing how you could do it
        trip = Trip(
            city_name=destination,
            package=1,  # Set a default package value or fetch from somewhere
            duration="3 days",  # Set a default duration or fetch from somewhere
            upcoming_trip_date=date
        )
        trip.save()

        return redirect('home')  # Redirect to the home page or wherever you want
    else:
        return HttpResponse('Invalid Request')
