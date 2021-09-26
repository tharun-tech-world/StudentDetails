from django.shortcuts import render, HttpResponse
from .models import Details


# Create your views here.


def index(request):
    # Getting data from the HTML and accepting
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        useremail = request.POST['useremail']
        graduation = request.POST['graduation']
        phone = request.POST['phone']
        activityname = request.POST['activityname']
        activityassigned = request.POST['activityassigned']
        print(firstname, lastname, useremail, graduation, phone, activityname, activityassigned)
        # Creating the Object of record every time user clicks on 'Add Data'
        obj = Details()
        obj.firstname = firstname
        obj.lastname = lastname
        obj.useremail = useremail
        obj.graduation = graduation
        obj.phone = phone
        obj.activityname = activityname
        obj.activityassigned = activityassigned
        obj.save()

    # Fetching the details and saving in an dictionary
    from django.core import serializers
    data = serializers.serialize("python", Details.objects.all())

    # Dictionary to store the data and send it back to HTML format
    context = {
        'data': data,
    }

    return render(request, 'index.html', context)


def next(request):
    # Getting data from the HTML and accepting
    return render(request, 'success.html')
