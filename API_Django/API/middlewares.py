from supabase import create_client
from dotenv import load_dotenv
import os
from django.http import JsonResponse
load_dotenv()

class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.supabase=create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
    def __call__(self, request):
        header = request.headers.get('Authorization')
        if not header:
            return JsonResponse({'error': 'Authorization header missing'}, status=401)
        token = header.split(' ')[1]
        if not token or len(header.split(' ')) != 2:
            return JsonResponse({'error': 'Token missing'}, status=401)
        try:
            response = self.supabase.auth.get_user(token)
            request.user_id=response.user.id
        except Exception as e:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        return self.get_response(request)