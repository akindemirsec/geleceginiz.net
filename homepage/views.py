from django.shortcuts import render
from core.models import Gn_user

def home(request):
    user_id = request.session.get('user_id')
    user = None
    if user_id:
        try:
            user = Gn_user.objects.get(userid=user_id)  # Burada user_id yerine id kullanmalısınız.
        except Gn_user.DoesNotExist:
            pass
    return render(request, 'homepage.html', {'user': user})
