from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lesson
from .forms import LessonForm
from .models import ActionLog

@login_required
def timetable(request):
    lessons = Lesson.objects.all()
    if request.user.role == 'student':
        lessons = lessons.filter(grade=request.user.grade)
    
    elif request.user.role == 'teacher':
        # 1. O'qituvchi faqat o'z darslarini ko'radi
        lessons = lessons.filter(teacher=request.user)
        # 2. Agar tepadagi menyudan sinf tanlangan bo'lsa (URL da ?grade=5 bo'lsa)
        selected_grade = request.GET.get('grade')
        if selected_grade:
            lessons = lessons.filter(grade=selected_grade)

    # Optimizatsiya: Barcha darslarni bitta so'rov bilan olib, vaqt bo'yicha saralaymiz
    lessons = lessons.order_by('start_time')
    
    # Python xotirasida kunlarga ajratamiz (DB ga 6 marta emas, 1 marta murojaat bo'ladi)
    days_dict = {'Mon': [], 'Tues': [], 'Wednes': [], 'Thurs': [], 'Fri': [], 'Satur': []}
    for lesson in lessons:
        if lesson.day in days_dict:
            days_dict[lesson.day].append(lesson)

    days_data = [
        ('Dushanba', days_dict['Mon']),
        ('Seshanba', days_dict['Tues']),
        ('Chorshanba', days_dict['Wednes']),
        ('Payshanba', days_dict['Thurs']),
        ('Juma', days_dict['Fri']),
        ('Shanba', days_dict['Satur']),
    ]
    return render(request, 'timetable.html', {'days_data': days_data})

@login_required
def lesson_create(request):
    if request.user.role != 'teacher':
        return redirect('timetable')

    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False) # Hozircha bazaga saqlamay turamiz
            lesson.teacher = request.user    # Dars egasi - hozirgi kirgan o'qituvchi

            # Vaqt to'qnashuvini tekshirish (Conflict check)
            if Lesson.objects.filter(
                teacher=request.user,
                day=lesson.day,
                start_time__lt=lesson.end_time,
                end_time__gt=lesson.start_time
            ).exists():
                form.add_error(None, "Bu vaqt oralig'ida allaqachon darsingiz bor!")
                return render(request, 'lesson_form.html', {'form': form})

            lesson.save()
            ActionLog.objects.create(
                user=request.user,
                action='Yaratdi',
                subject=lesson.subject
            )
            return redirect('timetable')     # Jadvalga qaytamiz
    else:
        form = LessonForm()
    return render(request, 'lesson_form.html', {'form': form})


@login_required
def lesson_update(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.user != lesson.teacher:
        return redirect('timetable')
        
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            ActionLog.objects.create(
                user=request.user,
                action="O'zgartirdi",
                subject=lesson.subject
            )
            return redirect('timetable')
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'lesson_form.html', {'form': form})

@login_required
def lesson_delete(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.user != lesson.teacher:
        return redirect('timetable')
        
    if request.method == 'POST':
        subject_name = lesson.subject  # O'chirishdan oldin nomini saqlab olamiz
        lesson.delete()
        ActionLog.objects.create(
            user=request.user,
            action="O'chirdi",
            subject=subject_name
        )
        return redirect('timetable')
    return render(request, 'lesson_confirm_delete.html', {'lesson': lesson})

@login_required
def action_history(request):
    # Faqat direktor kira oladi
    if request.user.role != 'director':
        return redirect('timetable')
    
    # Barcha loglarni vaqt bo'yicha teskari tartibda (eng yangisi tepada) olamiz
    logs = ActionLog.objects.all().order_by('-timestamp')
    
    return render(request, 'action_history.html', {'logs': logs})
