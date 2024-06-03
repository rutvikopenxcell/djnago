from django.http import HttpResponse
from django.template import loader
from .models import Member


# Create your views here.
def members(request):
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())
     mymembers = Member.objects.all().values()
     template = loader.get_template('all_members.html')
     context = {
     'mymembers': mymembers,
     }
     return HttpResponse(template.render(context, request))
