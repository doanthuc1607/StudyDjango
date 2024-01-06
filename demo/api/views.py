from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import ToDo
from .serializers import ToDoSerializer


@api_view(['GET'])
def getData(request):
    todos = ToDo.objects.all()
    serializer = ToDoSerializer(todos, many=True)
    return Response(serializer.data)

#post: create a new resource or submit data to be processed to a specified resource on the server
@api_view(['POST'])
def addTodo(request):
    serializer = ToDoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# create or update resource, override resource if it exists on the server
@api_view('PUT')
def updateTodo(request, pk):
    task = ToDo.objects.get(id=pk)
    serializer = ToDoSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTodo(request, pk):
    task = ToDo.objects.get(id=pk)
    task.delete()
    return Response('Item successfully delete!')