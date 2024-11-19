from django.contrib import admin

from django.contrib import admin
from .models import Customer,Designer,Admin,InteriorStyle,ThreeDView,Project,Feedback

admin.site.register(Customer)
admin.site.register(Designer)
admin.site.register(Admin)
admin.site.register(InteriorStyle)
admin.site.register(ThreeDView)
admin.site.register(Project)
admin.site.register(Feedback)

