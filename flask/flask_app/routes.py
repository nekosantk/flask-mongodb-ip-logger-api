from datetime import datetime, timezone
from flask_app import app
from flask import request
from .models import IpAccessLog


@app.get("/api/myip")
def get_my_ip():

    # Grab IP
    current_ip_address = request.headers.get('X-Real-IP', request.remote_addr)

    # Use UTC as the base timezone
    current_timestamp = datetime.utcnow().replace(tzinfo=timezone.utc)

    # Grab document from database
    ip_access_log = IpAccessLog.objects(ip_address=current_ip_address).first()

    # Check if this is first time access and set an appropriate response message
    if ip_access_log is None:

        # Set response message
        response_message = f"Your client’s IP address is: {current_ip_address}. " \
                           f"This is the first message received from your client.\n"

        # Create new document
        ip_access_log = IpAccessLog(ip_address=current_ip_address)

    else:
        # Formatted datetime into required format
        formatted_timestamp = ip_access_log.last_accessed_timestamp \
            .strftime("%a %b %m %H:%M:%S %Z %Y")

        # Instructions mention EDT/EST timezone, so not sure
        # if a conversion is wanted
        # formatted_timestamp = current_timestamp \
        #     .astimezone(ZoneInfo('US/Eastern')) \
        #     .strftime("%a %b %m %H:%M:%S %Z %Y")

        # Set response message
        response_message = f"Your client’s IP address is: {current_ip_address}. Your " \
                           f"previous/last request was on {formatted_timestamp}\n"


    # Set new timestamp and save
    ip_access_log.last_accessed_timestamp = current_timestamp
    ip_access_log.save()

    # Return response
    return response_message, 200
