from django.contrib import admin
from medicines.models import Registration,Contact, MedicineOrdered, Askdoctor, Contactlogin
admin.site.register(Registration)
admin.site.register(Contact)
admin.site.register(MedicineOrdered)
admin.site.register(Askdoctor)