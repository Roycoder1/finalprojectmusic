from django.contrib import admin

from .models import UserProfile,Photo,City,Contact

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Photo)
admin.site.register(City)
admin.site.register(Contact)
