from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from quality_control.forms import NewQuestionForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from quality_control.models import Questions, Regimes

#Add Regimes
@login_required(login_url='main_app:login')

def regimes(request):
	
	regimes_list = Regimes.objects.filter(is_deleted=False)

	context={
		"reasons_list" : regimes_list
	}
	return render(request, 'tracesavvy/apps/quality_control/regimes.html',context)

#Questions & Answers
@login_required(login_url='main_app:login')

def qa(request):

	qa_list = Questions.objects.all()

	context={
		"qa_list" : qa_list
	}
	return render(request, 'tracesavvy/apps/quality_control/qa.html',context)

# add question
@login_required(login_url='main_app:login')

def add_question(request):
	if request.method == 'POST':
		form = NewQuestionForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
				
			messages.success(request,f'Reason Created successfully')
			return redirect('main_app:add-question')
	
	else:
		form = NewQuestionForm()

	return render(request, 'tracesavvy/apps/quality_control/qa.html', {'form': form})
