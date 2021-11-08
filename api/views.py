from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.models import User, Advisor, Booking
from api.serializers import UserSerializer, AdvisorSerializer, BookingSerializer, BookingSerializerGet
from .util import encode, decode
import io

# parse byte content, byte data obtained from serializer 
def parse_data(content):
    stream = io.BytesIO(content)
    data = JSONParser().parse(stream)
    return data

@csrf_exempt  # please find explaination at the bottom 
def user_create_or_list(request):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        keys = data.keys()
        if "email" not in keys or "name" not in keys or "password" not in keys:
            return HttpResponse("400_BAD_REQUEST")
        user_exists = User.objects.filter(email= data["email"])
        if user_exists:
            return HttpResponse("201_USER_EXISTS")
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            content = JSONRenderer().render(serializer.data)
            content_ = parse_data(content)
            print(content_)
            response_data = {"UserId": content_["id"], "JWT_Token":encode({"userId": content_["id"], "role":"user"})}
            return JsonResponse(response_data,status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_login(request):

    if request.method=="POST":
        data = JSONParser().parse(request)
        try:
            snippet = User.objects.filter(email=data["email"])[0]
        except User.DoesNotExist:
            return HttpResponse(status = "HTTP_404_NOT_FOUND")

        serializer = UserSerializer(snippet)
        content = JSONRenderer().render(serializer.data)
        user = parse_data(content)
        if "email" not in data.keys() and "password" not in data.keys():
            return HttpResponse("400_BAD_REQUEST")
        if not user:
            return HttpResponse("400_BAD_REQUEST")
        elif user["password"]!= data["password"]:
            return HttpResponse("401_AUTHENTICATION_ERROR")
        # print(user[0], user[1])
        response_data = {"UserId": user["id"], "JWT_Token": encode({"userId": user["id"], "role":"user"})}
        return JsonResponse(response_data,status=200)

            
@csrf_exempt
def advisor_create_or_list(request, userId=None):
    """
    List all advisors, or create a new advisor.
    """
    if request.method == 'GET':
        advisors = Advisor.objects.all()

        serializer = AdvisorSerializer(advisors, many=True)
        print(serializer)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdvisorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('200_OK')
        return HttpResponse('400_BAD_REQUEST')
        
@csrf_exempt
def book_advisor_call(request, userId, advisorId):
    if request.method=="POST":
        data = JSONParser().parse(request)
        if "bookingTime" not in data.keys() or not userId or not advisorId:
            return HttpResponse("400_BAD_REQUEST")
        print(userId, advisorId)
        booking_data = {"time": datetime.datetime.fromisoformat(data["bookingTime"]), "user": int(userId), "advisor": int(advisorId)}
        serializer = BookingSerializer(data = booking_data)
        print(serializer.initial_data, serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("200_OK")
        return HttpResponse("400_BAD_REQUEST")


@csrf_exempt
def list_booking(request, userId):
    if request.method=="GET":
        try:
            booking_data = Booking.objects.filter(user_id= userId)
            data =[]
            for b in booking_data:
                res_data = BookingSerializerGet(b)
                data.append(res_data.data)
            for d in data:
                del d['user']
                d["booking_id"] = d["id"]
                d["booking_time"] = d["time"]
                d['advisor_name'] = d["advisor"]["name"]
                d["advisor_id"]   = d["advisor"]["id"]
                d["advisor_photo"] = d["advisor"]["photoUrl"]
                del d["advisor"]; del d["id"]; del d["time"]
            return JsonResponse(data, safe=False)

        except Booking.DoesNotExist:
            return HttpResponse("400_BAD_REQUEST")
            


# Normally when you make a request via a form you want the form being submitted to your view to originate from your website and 
# not come from some other domain. To ensure that this happens, you can put a csrf token in your form for your view to recognize. 
# If you add @csrf_exempt to the top of your view, then you are basically telling the view that it doesn't need the token.
# This is a security exemption that you should take seriously.
# As here we are using this  as API's