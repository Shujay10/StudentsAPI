from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json


@csrf_exempt
def books(request):
    if request.method == 'GET':
        students = Student.objects.all().values()
        return JsonResponse({"students": list(students)})
    elif request.method == 'POST':
        # To create post request in url
        # title = request.POST.get('title')
        # author = request.POST.get('author')
        # price = request.POST.get('price')

        # To create post request in body
        json_string = request.body
        json_data = json.loads(json_string)

        students = Student(**json_data)

        # books = Book(
        #         title = title,
        #         author = author,
        #         price = price
        #     )

        try:
            students.save()
        except IntegrityError:
            return JsonResponse({'success': 'false', 'message': 'required field missing'}, status=400)

        return JsonResponse(model_to_dict(students), status=201)
