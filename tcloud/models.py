from django.db import models

#Create your models here.
class Course(models.Model):
	coursename=models.CharField(max_length=100,primary_key=True)

	def __str__(self):
		return self.coursename


class Advertisement(models.Model):
	adv_name=models.CharField(max_length=100,primary_key=True)
	def __str__(self):
		return self.adv_name


class Details(models.Model):
	class meta:
		unique_together = (('mobile', 'email'),)
	name=models.CharField(max_length=100)
	mobile=models.IntegerField(primary_key=True)
	email=models.EmailField()
	course=models.ForeignKey(Course,on_delete=models.CASCADE)
	Advertisement=models.ForeignKey(Advertisement,on_delete=models.CASCADE)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)

	def __str__(self):
		return str(self.mobile)


class joined(models.Model):
	stu_list=(('f','followup'),('j','join'),('i','ignore'))
	#details=CompositeForeignKey(Details,on_delete=models.CASCADE,related_name=joines,to_fields={'mobile':'mobile number','email':'email_id'})
	mobile=models.ForeignKey(Details,on_delete=models.CASCADE,related_name='one')
	#email=models.ForeignKey(Details,on_delete=models.CASCADE,related_name='two')
	email=models.EmailField()
	enquire1=models.TextField()
	enquire2=models.TextField()
	enquire3=models.TextField()
	enquire4=models.TextField()
	enquire5=models.TextField()
	status=models.CharField(max_length=100,choices=stu_list)
	update=models.DateTimeField(auto_now_add=False,auto_now=True)
