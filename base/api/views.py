from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room, Topic, extra
from .serializers import LoginSerializers, RoomSerializers, TopicSerializers, todoSerializers, RegisterSerializers,LoginSerializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


@api_view(['GET'])
def getRoutes(request):

    routes = [
        'GET /api/',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'POST /api/room/:id/create',
        'PUT /api/room/:id/edit',

        # different
        'GET /api/todo',
        'POST /api/todo/create',
        'PUT /api/todo/update/:id',
        'DELETE /api/todo/delete/:id',

        # login signup
        'POST /api/register',
        'POST /api/Login',
    ]
    return Response(routes)


#  THIS GIVES ERROR
# @api_view(['GET'])
# def getRooms(request):
#     rooms=Room.objects.all()
#     return Response(rooms)

# correct
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializers(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSingleRoom(request, pk):
    rooms = Room.objects.get(id=pk)
    serializer = RoomSerializers(rooms, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def newRoom(request):
    serializer = RoomSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def topics(request):
    topic = Topic.objects.all()
    serializer = TopicSerializers(topic, many=True)
    return Response(serializer.data)


# request.data works for put post patch also


@api_view(['GET'])
def todo_all(request):
    extras = extra.objects.all()
    serializer = todoSerializers(extras, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def todo_create(request):
    serializer = todoSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response('New data added')


@api_view(['PUT'])
def todo_update(request, pk):
    extras = extra.objects.get(id=pk)
    serializer = todoSerializers(instance=extras, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('updated successfully')


@api_view(['DELETE'])
def todo_delete(request, pk):
    extras = extra.objects.get(id=pk)
    extras.delete()
    return Response('Item deleted successfully')


# login

@api_view(['POST'])
def loginUser(request):
    if request.method=="POST":
        serializer = LoginSerializers(data=request.data)
    data={}
    if serializer.is_valid():
       user= serializer.save()
       return Response("Logged in")
    return Response('Enter the data')
    # username = user.username
    # password = user.password

    # try:
    #     user = User.objects.get(username=username)
    # except:
    #     return Response('User does not exist')

    #     # error or give a user object of the user
    # user = authenticate(request, username=username, password=password)

    # if user is not None:
    #     # create a session id in the cookies
    #     login(request, user)
    #     return Response(data)

    # else:
    #     return Response('Invalid data')

# register a user
@api_view(['POST'])
def registration_view(request):

    if request.method=='POST':
        serializer=RegisterSerializers(data=request.data)
        data ={}
        if serializer.is_valid():
            User= serializer.save()
            data['response']='Successfully registered'
            data['email']=User.email
            data['username']=User.username
        else :
            data=serializer.errors
        return Response(data)