from django.contrib import admin
from .models import UserDetails,Activity,Workout,Goal,Leaderboard


# Register your models here.

admin.site.register(UserDetails)
admin.site.register(Activity)
admin.site.register(Workout)
admin.site.register(Goal)
admin.site.register(Leaderboard)
