from django.contrib import admin
from contact.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('contact_name', 'contact_email', 'contact_sub', 'contact_message')

admin.site.register(Contact, ContactAdmin)