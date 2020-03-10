from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from forms.models import FormModel
from rest_framework.parsers import JSONParser
from forms.serializers import FormModelSerializer
from StackFusion.mailer import Mailer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def data(request):
    data = FormModel.objects.all()
    if request.method == 'GET':
        serializer = FormModelSerializer(data, many=True)
        # mail = Mailer()
        # mail.send_messages(subject='My App account verification',
        #                    template='email.html',
        #                    context={'customer': mail},
        #                    to_emails=['leoghsay@gmail.com'])

        return JsonResponse(serializer.data, safe=False,status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = FormModelSerializer(data=data)
        # print(serializer.error_messages)
        # print(serializer.is_valid())
        if serializer.is_valid(raise_exception=True):
            # print(serializer.validated_data)
            serializer.save()
            print(serializer.data)
            return JsonResponse(serializer.data, status=201)
        return HttpResponseRedirect("/error")
    elif request.method == "OPTIONS":
        return HttpResponseRedirect("/error")
    #     {
    #         res.writeHead(200, {"Content-Type": "application/json"});
    #     res.end();
    #     }

# Create your views here.
