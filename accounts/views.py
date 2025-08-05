from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import SignupForm

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': '잘못된 JSON 형식입니다.'}, status=400)

        form = SignupForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': '회원가입 성공'}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'message': 'POST 요청만 허용됩니다'}, status=405)