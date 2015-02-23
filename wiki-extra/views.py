from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def index(request):
    return HttpResponse("{0:s}".format(request.user.first_name))