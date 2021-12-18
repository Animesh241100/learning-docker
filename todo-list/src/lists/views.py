from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from lists.models import Task
from lists.serializers import TaskSerializer



class GetTasksList(APIView):
    def get(self, request, format=None):
        task_objs = Task.objects.all()
        task_serializer = TaskSerializer(task_objs, many=True)
        return Response(task_serializer.data, status=status.HTTP_200_OK)


class CreateTask(APIView):
    def post(self, request, format=None):
        name = request.data["name"]
        is_completed = request.data["is_completed"]
        Task.objects.create(name=name, is_completed=is_completed)
        return Response(status=status.HTTP_200_OK)


class UpdateTask(APIView):
    def post(self, request, format=None):
        try:
            task_obj = Task.objects.get(pk=request.data["id"])
            task_obj.name = request.data["name"]
            task_obj.is_completed = request.data["is_completed"]
            task_obj.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DeleteTask(APIView):
    def delete(self, request, format=None):
        try:
            task_obj = Task.objects.get(pk=request.data["id"])
            task_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


