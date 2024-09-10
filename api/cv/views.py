from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Curriculum, Education, Experience
from .serializers import CurriculumSerializer, EducationSerializer, ExperienceSerializer

class CurriculumAPIView(APIView):

    def post(self,request):
        serializer=CurriculumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        curriculums=Curriculum.objects.all()
        serializer=CurriculumSerializer(curriculums,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CurriculumDetailAPIView(APIView):

    def get(self,request,id):
        if Curriculum.objects.filter(id=id).exists():
            curriculum=Curriculum.objects.get(id=id)
            serializer=CurriculumSerializer(curriculum)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error':'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self,request,id):
        curriculum=Curriculum.objects.get(id=id)
        if curriculum is None:
            return Response({'error':'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=CurriculumSerializer(curriculum,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        curriculum=Curriculum.objects.get(id=id)
        if curriculum is None:
            return Response({'error':'Not found'}, status=status.HTTP_404_NOT_FOUND)
        curriculum.delete()
        return Response({'message':'Curriculum deleted successfully'}, status=status.HTTP_200_OK)
    
class EducationListCreateAPIView(generics.ListCreateAPIView):
    queryset=Education.objects.all()
    serializer_class=EducationSerializer

class EducationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Education.objects.all()
    serializer_class=EducationSerializer

class ExperienceListCreateAPIView(generics.ListCreateAPIView):
    queryset=Experience.objects.all()
    serializer_class=ExperienceSerializer

class ExperienceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Experience.objects.all()
    serializer_class=ExperienceSerializer