from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from api.models import Owner, Properties

class SerializerUserLogin(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        
        user = authenticate(username=attrs["username"], password=attrs["password"])
        if user is  None:
            
            raise serializers.ValidationError('Usuario o contraseña incorrecta')
            
        self.context['user'] = user
        return attrs
    
    
    def create(self, validated_data):
        user = self.context['user']
        
        try:
            token=Token.objects.get(user_id=user.id )
        except:
            token = Token.objects.create(user=user)   
        
        print(token.key)
        
        return user,token
    
class SerializerUserRegister(serializers.Serializer):
    username = serializers.CharField()
    password1 = serializers.CharField(min_length=6)
    password2 = serializers.CharField(min_length=6)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    
    

    def validate(self, attrs):
        
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError('Las contraseñas deben coincidir') 
        user = User.objects.filter(username=attrs["username"])
        
        if user:
            raise serializers.ValidationError('Este usuario ya existe')
            
        
        
        
        return attrs



    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        try:    
            user = User.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError(e)
        
        user.set_password(password)
        user.save()
        
        
        
        
        return user   
    
class SerializerOwner(serializers.ModelSerializer):
    class Meta:  
        model = Owner
        fields = '__all__'
        
        
class SerializerProperties(serializers.ModelSerializer):
    propietario_name = serializers.SerializerMethodField()

    def get_propietario_name(self,obj):
        return obj.propietario.name
        
        
    class Meta:  
        model = Properties
        fields = '__all__'



    
    