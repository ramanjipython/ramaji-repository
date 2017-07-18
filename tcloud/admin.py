from django.contrib import admin
from .models import Course,Advertisement,Details,joined


class CourseAdmin(admin.ModelAdmin):

	field='course'

class DetailsAdmin(admin.ModelAdmin):
	list_display=['name','mobile','email','timestamp']
	list_filter=['name','mobile']


class joinedAdmin(admin.ModelAdmin):
	list_display=['mobile','email','status']
	list_filter=['status']




admin.site.register(Course,CourseAdmin)
admin.site.register(Advertisement)
admin.site.register(Details,DetailsAdmin)
admin.site.register(joined,joinedAdmin)

