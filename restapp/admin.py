from django.contrib import admin
from .models import User, Client, Server, Camera, Exiting, Entering



class userAdmin(admin.ModelAdmin):

	fields = [
	'firstname',
	'lastname',
	'username',
	'password',
	'createdat',
	'updatedat',
	]
	readonly_fields = [
	'createdat',
	'updatedat'
	]

admin.site.register(User,userAdmin)
admin.site.register(Client)
admin.site.register(Server)
admin.site.register(Camera)
admin.site.register(Exiting)
admin.site.register(Entering)