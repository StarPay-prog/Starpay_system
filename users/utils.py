import random
import time
from .models import Journal  # Replace 'yourapp' with the actual name of your Django app

def generate_unique_transaction(balance, email, amount, booking_id):
    while True:
        # Extract relevant information

        
        # Use timestamp to ensure uniqueness
        timestamp = int(time.time() * 1000)  # Current time in milliseconds
        
        # Generate a random component with both lowercase and uppercase characters
        random_component = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=4))
        
        # Concatenate relevant details, timestamp, and random component
        details_str = f"{balance}-{email}-{amount}-{booking_id}-{timestamp}-{random_component}"
        
        # Hash the combined details
        hashed_details = hash(details_str)

        # Use a portion of the hashed value as the booking ID
        unique_id = str(hashed_details % 100000000)
        
        # Form the complete booking ID
        Transaction_id = f"TRP-TRAN-ID-{unique_id}"

        # Check if the generated booking ID already exists in the database
        if not Journal.objects.filter(Transaction_id=Transaction_id).exists():
            return Transaction_id
        
transaction_status_choices=(("Success","Success"),
                 ("In Progress","In Progress"),
                 ("On Hold","On Hold"),
                 ("Failed","Failed"),
                 ("Pending","Pending"),
                 ("Aborted","Aborted"),
                 ("Unconfirmed","Unconfirmed"),
                 ("Cancelled","Cancelled")
                 )