from rest_framework import serializers
from .models import Estabelecimento, Sala, Jammer

class CadastroSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirmarEmail = serializers.CharField(write_only=True)
    class Meta:
        fields = ['email', 'password', 'confirmarEmail']
    def validate(self, data):
        if data['password'] != data['confirmarEmail'] or not data['email'] or not data['password'] or not data['confirmarEmail']:
            raise serializers.ValidationError("Todos os campos são obrigatórios ou as senhas não coincidem.")
        return {
            'email': data['email'],
            'password': data['password'],
        }

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    class Meta:
        fields = ['email', 'password']
    def validate(self, data):
        if not data['email'] or not data['password']:
            raise serializers.ValidationError("Todos os campos são obrigatórios.")
        return {
            'email': data['email'],
            'password': data['password'],
        }
class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = '__all__'
    

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'


class JammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jammer
        fields = '__all__'