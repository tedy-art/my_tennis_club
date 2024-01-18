from django.http import HttpResponse
from django.template import loader
from .models import Member


# Create your views here.
def members(request):
    """
    - Creates a mymembers object with all the values of the Member model.
    - Loads the all_members.html template.
    - Creates an object containing the mymembers object.
    - Sends the object to the template.
    - Outputs the HTML rendered by the template.
    """
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    """
    The details view does the following:
        - Gets the id as an argument.
        - Uses the id to locate the correct record in the Member table.
        - loads the details.html template.
        - Creates an object containing the member.
        - Sends the object to the template.
        - Outputs the HTML that is rendered by the template.
    """
    mymember = Member.objects.get(id = id)
    template = loader.get_template("details.html")
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits':["apple", "banana", "cherry"],
    }
    return HttpResponse(template.render(context, request))