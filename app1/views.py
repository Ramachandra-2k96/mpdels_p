from django.shortcuts import render
from .forms import inputform
from .models import StudentRegistration
# Create your views here.
def home(request):
    if request.method=="POST":
        form=inputform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'app1/index.html',{"param1":"Form submitted successfully",'form':form})
    else:
        form=inputform()
    return render(request,'app1/index.html',{"form":form})

def certificate(request):
    users=StudentRegistration.objects.all()
    str1='Certificate of Completion'
    str2='this is to certify that'
    str3='from'
    str4=' has participated in'
    str5='held from 6 th May 2024.'
    for user in users:
        with open(f'certificate_{user.name}.txt','w')as certi:
            certi.write(f'{str1}\n{str2} {user.name} {str3} {user.college_name} {str4} {user.course_name} {str5}')
    strings={
		'str1':str1,
		'str2':str2,
		'str3':str3,
		'str4':str4,
		'str5':str5,
	}
    return render(request,'app1/certificate.html',{'users':users,'param2':strings})