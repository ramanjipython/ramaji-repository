from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from tcloud.forms import StudentForm,JoinedForm

# Create your views here.

def hellow(request):
	return HttpResponse("Hello!! world \n")



def Student(request):
	form=StudentForm
	context={'form':form}

	if request.method == 'POST':
		form = StudentForm(request.POST)
		
		if form.is_valid():
			name=form.cleaned_data['name']
			mobile=form.cleaned_data['mobile']
			email=form.cleaned_data['email']
			enquire_date=form.cleaned_data['enqiure_data']
			join_date=form.cleaned_data['join_date']
			subject= 'A new student {}'.format(mobile)
			return HttpResponseRedirect('/tcloud/thanks/')
		else:
			return render(request,'StudentForm.html',context)
	return render(request,'StudentForm.html',context)




def Joined(request):
	form=JoinedForm
	context={'form':form}

	if request.method == 'POST':
		form=JoinedForm(request.POST)
		


		if form.is_valid():
			mobile=form.cleaned_data['mobile']
			enquire1=form.cleaned_data['enquire1']
			enquire1=form.cleaned_data['enquire2']
			enquire1=form.cleaned_data['enquire3']
			enquire1=form.cleaned_data['enquire4']
			enquire1=form.cleaned_data['enquire5']
			status=form.cleaned_data['status']
			return HttpResponseRedirect('/tcloud/thanks')
		else:
			return render(request,'JoinedForm.html',context)

	return render(request,'JoinedForm.html',context) 

		
