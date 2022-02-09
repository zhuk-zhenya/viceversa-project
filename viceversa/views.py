from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')
	

def reverse(request):
	user_text = request.GET['usertext']
	word_count = len(user_text.split())
	reverse_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text,'reverse_text':reverse_text, 'word_count':word_count})
	