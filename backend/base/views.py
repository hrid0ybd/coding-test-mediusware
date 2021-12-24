from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from rest_framework.response import Response
# from rest_framework.serializers import Serializer
# from rest_framework.views import APIView


# View Frontend
def index(request):
    return render(request, 'build/index.html')

# # Models
# from base.models import Persons
# from base.serializers import PersonSerializer

# @csrf_exempt
# # API Method for persons
# def personApi(request, id=0):
#     if (request.method == 'GET'):
#         persons = Persons.objects.all()
#         persons_serializer = PersonSerializer(persons, many=True)
#         return JsonResponse(persons_serializer.data, safe=False)

#     elif (request.method == 'POST'):
#         person_data = JSONParser().parse(request)
#         persons_serializer = PersonSerializer(data=person_data)

#         # If valid save it to database
#         if persons_serializer.is_valid():
#             persons_serializer.save()
#             return JsonResponse("Person added successfully!", safe=False)

#         return JsonResponse("Failed to add person information", safe=False)

#     elif (request.method == 'PUT'):
#         person_data = JSONParser().parse(request)
#         person = Persons.objects.get(personId=person_data['personId'])
#         persons_serializer = PersonSerializer(person, data=person_data)

#         if persons_serializer.is_valid():
#             persons_serializer.save()
#             return JsonResponse("Person information updated successfully", safe=False)
#         return JsonResponse("Failed to update person information", safe=False)

#     elif (request.method == 'DELETE'):
#         person = Persons.objects.get(personId=id)
#         person.delete()
#         return JsonResponse("Person information has deleted successfully", safe=False)
