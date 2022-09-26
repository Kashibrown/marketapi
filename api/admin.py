from django.contrib import admin
from .models import Market

#i would be adding this model to the admin because i saved some data there , 
#you can also use the python manage.py shell to save information into our database 
admin.site.register(Market)