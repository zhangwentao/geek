# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,HttpResponseRedirect
from django.template import RequestContext
from simplejson.encoder import JSONEncoder
from models import Topic

def writeTopic(request):
	topic_name = request.POST['topic']
	sender_name = request.POST['name']		
	topic_record = Topic()
	topic_record.sender_name = sender_name
	topic_record.topic_name = topic_name
	topic_record.save()
	return HttpResponse("ok");

def readTopic(request):
	topics = Topic.objects.all()
	result = ''
	if len(topics) > 0:
		topic = topics[0]
		result = '{"topic":"'+topic.topic_name+'","name":"'+topic.sender_name+'"}'
		topic.delete()
	else:
		result='none'
	return HttpResponse(result) 

def home(request):
	return render_to_response("home1.html",{},context_instance=RequestContext(request))
