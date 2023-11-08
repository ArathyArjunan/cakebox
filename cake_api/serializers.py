from rest_framework import serializers
from cakeapp.models import User,Cakes,CakeVarients


class Userserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(read_only=True)


    class Meta:
        model=User
        fields=["id","username","password","email","phone","address"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class CakeVarientSerializer(serializers.ModelSerializer):

    class Meta:
        model=CakeVarients
        fields="__all__"

class  CakeSerializer(serializers.ModelSerializer):
    Category=serializers.StringRelatedField(read_only=True)
    varients=CakeVarientSerializer(many=True,read_only=True)
    
    
    class Meta:
        model=Cakes
        fields="__all__"

    


