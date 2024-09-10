from rest_framework import serializers
from .models import Curriculum, Education, Experience


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class CurriculumSerializer(serializers.ModelSerializer):
    education=EducationSerializer(many=True, read_only=True)
    experience=ExperienceSerializer(many=True, read_only=True)
    class Meta:
        model = Curriculum
        fields = '__all__'



