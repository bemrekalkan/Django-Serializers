from rest_framework import serializers
from .models import Path, Student

# 1.yöntem
# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)  # null true olanlar için required false vermemiz gerekiyor.
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance


#2. yöntem

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = ["id", "path_name"]


class StudentSerializer(serializers.ModelSerializer):

    # full_name = serializers.SerializerMethodField()
    # def get_full_name(self, obj):
    #     return f'{obj.first_name} - {obj.last_name}'
    path = serializers.StringRelatedField()
    path_id = serializers.IntegerField()
    class Meta:
        model = Student
        fields = ["id", "path_id", "path", "first_name", "last_name", "number"]
        # fields = '__all__' # hepsini getir
        # exclude = ['number']  # numbers haricini getir.
