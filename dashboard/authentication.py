from functools import wraps
from django.shortcuts import redirect
from .models import CustomSession  # Import your CustomSession model

def custom_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check if user information is present in session data
        if 'user_data' not in request.session:
            # Redirect the user to the login page or any other page as needed
            return redirect('user-logout')  # Adjust 'login' to your login URL name
               
        # Get the user's IP address from your custom session model
        try:
            custom_session = CustomSession.objects.get(session=request.session.session_key)
            session_ip = custom_session.IP
        except CustomSession.DoesNotExist:
            # Handle the case where session data is not found
            print('session not found')
            return redirect('user-logout')
            session_ip = None
        
        # Add additional checks here if needed
        user_ip = request.META.get('REMOTE_ADDR')
    
   
        forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded_for:
            user_ip = forwarded_for.split(',')[0].strip()

        # Example: Check if the IP address matches a certain value
        if user_ip != session_ip:
            # Redirect the user to a different page if IP doesn't match
            return redirect('user-logout')  # Adjust 'invalid_ip' to your URL name
        
        # Continue with the view function if all checks pass
        return view_func(request, *args, **kwargs)
    return wrapper
