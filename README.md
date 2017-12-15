# chatRoom
A simple chat application that enables user to send and receive messages in realtime  

### Installation

Create a virtualenv for the project, and run:

```pip install -r requirements.txt```

Make sure Redis is running locally as the settings are configured to point to ```localhost```, port 6379, but you can change this in the ```CHANNEL_LAYERS``` setting ```in settings.py```.

Run python ```manage.py migrate```

To make an account run 
```python manage.py createsuperuser```

Then run ```python manage.py runserver```

