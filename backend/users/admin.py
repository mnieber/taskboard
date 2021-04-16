from django.contrib import admin

from users import models


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.User)
admin.site.register(models.Profile, ProfileAdmin)
