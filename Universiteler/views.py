from django.shortcuts import get_object_or_404, render
from core.models import Gn_universite, Gn_user, Gn_Fakulte, Gn_Bolum, Course

def universiteler(request):
    user_id = request.session.get('user_id')
    user = None
    if user_id:
        try:
            user = Gn_user.objects.get(userid=user_id) 
        except Gn_user.DoesNotExist:
            pass
    universities = Gn_universite.objects.all()
    return render(request, 'universiteler.html', {'universities': universities, "user": user})

def uni_fakulteler(request, uni_id):
    user_id = request.session.get('user_id')
    user = None
    if user_id:
        try:
            user = Gn_user.objects.get(userid=user_id) 
        except Gn_user.DoesNotExist:
            pass
    universite = get_object_or_404(Gn_universite, pk=uni_id)
    fakulteler = Gn_Fakulte.objects.filter(fakulte_uni=universite)
    return render(request, 'uni_fakulteler.html', {'universite': universite, 'fakulteler': fakulteler, "user": user})

def fakulte_bolumler(request, fakulte_id):
    user_id = request.session.get('user_id')
    user = None
    if user_id:
        try:
            user = Gn_user.objects.get(userid=user_id) 
        except Gn_user.DoesNotExist:
            pass
    fakulte = get_object_or_404(Gn_Fakulte, pk=fakulte_id)
    bolumler = Gn_Bolum.objects.filter(bolum_fakulte=fakulte)
    return render(request, 'fakulte_bolumler.html', {'fakulte': fakulte, 'bolumler': bolumler, "user": user})

def bolum_courses(request, bolum_id):
    user_id = request.session.get('user_id')
    user = None
    if user_id:
        try:
            user = Gn_user.objects.get(userid=user_id) 
        except Gn_user.DoesNotExist:
            pass
    bolum = get_object_or_404(Gn_Bolum, pk=bolum_id)
    courses = Course.objects.filter(bolum=bolum)
    return render(request, 'bolum_courses.html', {'bolum': bolum, 'courses': courses, "user": user})

def course_detail(request, course_id):
    user_id = request.session.get('user_id')
    user = None
    if user_id:
        try:
            user = Gn_user.objects.get(userid=user_id) 
        except Gn_user.DoesNotExist:
            pass
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_detail.html', {'course': course, "user": user})
