from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect


def home(request):
    """
    The first place when user access the website. If user is authenticated then redirect to the app.
    :param request: WSGI request from user.
    :return: The home for guest or redirect to the app if user is authenticated.
    """
    if request.user.is_authenticated:
        return redirect('drive')
    return render(request, 'emergency/home.html')


@login_required
def drive(request):
    """
    The main page for the app. This page use to track the user's location when user is driving.
    :param request: WSGI request from user.
    :return: Render the page and pass the value from context to the template (drive.html)
    """
    parameter = {
        'user': request.user,
        'background_image': 'img/943545.jpeg'
    }
    return render(request, 'emergency/drive.html', parameter)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def staff(request):
    """
    The page for the staff. It's used to manage the accident or emergency and manage the user information too.

    This page is only accessible for the staff and superuser.

    :param request: WSGI request from user.
    :return: Render the page and pass the value from context to the template (staff.html)
    """
    parameter = {
        'user': request.user,
        'background_image': 'img/943545.jpeg'
    }
    return render(request, 'emergency/staff.html', parameter)