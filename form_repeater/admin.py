from django.contrib import admin
from .models import *

admin.site.register(InspectionForm)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Option)
admin.site.register(OptionTitle)

