from django.http import HttpResponse
from django.template import Context, loader
from polls.models import Poll

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = Context({
		'latest_poll_list': latest_poll_list,
	})
	#output = ', '.join([p.question for p in latest_poll_list])
	return HttpResponse(template.render(context))

def detail(request, poll_id):
	return HttpResponse("You're looking at polls %s." % poll_id)

def results(request, poll_id):
	return HttpResponse("You're looking at the results of polls %s." % poll_id)
	
def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)
