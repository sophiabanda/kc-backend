from django.contrib import admin
from .models import React

# Register your models here.
from django.contrib import admin
from .models import React

class ReactAdmin(admin.ModelAdmin):
    fields = ['name', 'biography']
    widgets = {
        'biography': admin.widgets.AdminTextareaWidget(attrs={'cols': 80, 'rows': 5}),
    }

admin.site.register(React, ReactAdmin)
