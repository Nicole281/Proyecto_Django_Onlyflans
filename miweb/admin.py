from django.contrib import admin
from .models import Flan, ContactForm
# Register your models here.

admin.site.register(Flan)

class ContactFormAdmin(admin.ModelAdmin):
    readonly_fields = ('contact_form_uuid', 'customer_name', 'customer_email', 'message')
    list_display = ('customer_name', 'customer_email', 'message', 'contact_form_uuid')
    search_fields = ('customer_name', 'customer_email', 'message')

# Register the ContactForm model with its admin class
admin.site.register(ContactForm, ContactFormAdmin)