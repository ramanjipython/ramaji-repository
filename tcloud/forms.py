from django import forms
from .models import joined


class StudentForm(forms.Form):
	name=forms.CharField(required=True)
	mobile=forms.IntegerField(required=True)
	email=forms.EmailField(required=True)
	enquire_date=forms.DateTimeField(required=True)
	join_date=forms.DateTimeField(required=True)



	def clean_mobile(self):
		mobile = self.cleaned_data['mobile']
		if mobile is None:
			raise forms.ValidationError("This value cannot be empty")
		else:
			if not mobile.isdigit():
				raise forms.ValidationError("Please enter a valid phone number.")
		return mobile





class JoinedForm(forms.Form):
	class meta:
		model=joined
		fields=['mobile','enquire1','enquire2','enquire3','enquire4','enquire5','status']


	def clean_mobile(self):
		mobile = self.cleaned_data['mobile']
		if mobile is None:
			raise forms.ValidationError("This value cannot be empty")
		else:
			if not mobile.isdigit():
				raise forms.ValidationError("Please enter a valid phone number.")
		return mobile



