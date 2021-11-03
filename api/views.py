from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.models import User, Advisor, Booking
from api.serializers import UserSerializer, AdvisorSerializer, BookingSerializer
import io
import datetime

def parse_data(content):
    stream = io.BytesIO(content)
    data = JSONParser().parse(stream)
    return data

@csrf_exempt
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
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            content = JSONRenderer().render(serializer.data)
            content_ = parse_data(content)
            print(content_)
            response_data = {"UserId": content_["id"], "JWT_Token":''}
            return JsonResponse(response_data,status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_login(request):

    if request.method=="POST":
        # print(request.body)
        data = JSONParser().parse(request)
        try:
            snippet = User.objects.all().filter(email=data["email"])[0]
        except User.DoesNotExist:
            return HttpResponse(status="400_BAD_REQUEST")

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
        response_data = {"UserId": user["id"], "JWT_Token":''}
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
        booking_data = {"time": datetime.datetime.fromisoformat(data["bookingTime"]), "user_id": int(userId), "advisor_id": int(advisorId)}
        serializer = BookingSerializer(data = booking_data)
        print(serializer.initial_data, serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("200_OK")
        return HttpResponse("400_BAD_REQUEST")


def helper(data):
    serializer = BookingSerializer(data)
    content = JSONRenderer().render(serializer.data)
    user = parse_data(content)
    return user
@csrf_exempt
def list_booking(request, user_id):
    if request.method=="GET":
        try:
            booking_data = Booking.objects.filter(user_id= user_id)
        except Booking.DoesNotExist:
            return HttpResponse("400_BAD_REQUEST")
        user = helper(booking_data)
        for user_ in user:
            booking = AdvisorSerializer(Advisor.objects.get(id=user_["advisor_id"]))
        if (booking_data):
            return JsonResponse(booking_data, 200),
        return HttpResponse(400)