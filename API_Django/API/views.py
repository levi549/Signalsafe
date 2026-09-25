from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from supabase import create_client
from dotenv import load_dotenv
import os
from .serializers import CadastroSerializer, LoginSerializer, EstabelecimentoSerializer, SalaSerializer, JammerSerializer
from .models import Estabelecimento, Sala, Jammer,User
# Create your views here.
load_dotenv()



@api_view(['POST'])
def cadastro(request):
    supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
    try:    
        data = request.data
        serializer = CadastroSerializer(data=data)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=400)
        
        response=supabase.auth.sign_up({
            "email": serializer.validated_data['email'],
            "password": serializer.validated_data['password']
        })
        return Response({
        "email":response.user.email,
        "session":response.session}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(['POST'])
def login(request):
    supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
    try:
        data=request.data
        serializer=LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=400)
        response = supabase.auth.sign_in_with_email_and_password(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        return Response({
            "email": response.user.email,
            "session": response.session
        }, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(['GET'])
def get_estabelecimento(request):
    try:
        estabelecimentos = Estabelecimento.objects.filter(id_user_id=user)
        serializer = EstabelecimentoSerializer(estabelecimentos, many=True)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(["GET"])
def get_sala(request):
    try:
        user=request.user_id
        id_estabelecimento= request.GET('id_estabelecimento')
        if not user or not id_estabelecimento:
            return Response({"error": "Something missing"}, status=400)
        salas = Sala.objects.filter(
            id_estabe_id=id_estabelecimento,
            id_estabe__id_user_id=user
         )
        serializer = SalaSerializer(salas, many=True)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(["GET"])
def get_jammer(request):
    try:
        user=request.user_id
        estabelecimento_id=request.GET.get('id_estabelecimento')
        sala_id=request.GET.get('id_sala')
        if not user or not estabelecimento_id or not sala_id:
            return Response({"error": "Something missing"}, status=400)
        jammers=Jammer.objects.filter(
            id_sala_id=sala_id,
            id_sala__id_estabe_id=estabelecimento_id,
            id_sala__id_estabe__id_user_id=user
        )
        serializer = JammerSerializer(jammers, many=True)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)



@api_view(['POST'])
def create_estabelecimento(request):
    try:
        user=request.user_id
        data=request.data
        if not data or not user:
            return Response({"error":"something is missing"},status=400)
        serializer=EstabelecimentoSerializer(data=data)
        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=400)
        serializer.save(id_user_id=user)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(['POST'])
def create_sala(request):
    try:
        user=request.user_id
        estabelecimento=request.GET.get('id_estabelecimento')
        data=request.data
        if not user or not data or not estabelecimento:
            return Response({"Error":"something is missing"},status=400)
        serializer=SalaSerializer(data=data)
        if not serializer.is_valid():
            return Response({"error":serializer.errors},status=400)
        serializer.save(id_estabe_id=estabelecimento,id_estabe__id_user_id=user)
        return Response(serializer.data,status=200)
    except Exception as e:
        return Response({"error":str(e)}, status=400)