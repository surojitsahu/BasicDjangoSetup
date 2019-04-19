from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def first_view(request):
	return HttpResponse('<h1>Hello this is my first view</h1>')

def second_view(request):
	return HttpResponse('<h4>Hello this my second view</h4>')

def time_info(request):
	time=datetime.datetime.now()
	s='<h1>hello current date and time is :'+str(time)+'</h1>'

	return render(request,'testapp/result.html',{'s':s})

def third_view(request):
	time=datetime.datetime.now()
	name='surojit'
	rollno=1001
	marks=67

	return render(request,'testapp/result.html',{'s':time,'name':name,'rollno':rollno,'marks':marks})


def wish(request):
		time=datetime.datetime.now()
		h=int(time.strftime('%H'))
		msg='Hello there !!! Very Good'
		if h<12:
			msg=msg+'Morning!!'
		elif h <16:
			msg=msg+'Afternoon!!'
		elif h<21:
			msg=msg+'Evening!!'
		else:
			msg=msg+'Night!!'

		return render(request,'testapp/result.html',{'msg':msg})			
			
		