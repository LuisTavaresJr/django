from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollment
from .forms import ContactCourse

# Create your views here.
def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)

# def details(request, pk):
#    course = get_object_or_404(Course, pk=pk)
#    context = {'course': course}
#    template_name = 'courses/details.html'
#    return render(request, template_name, context)

def details(request, slug):
   course = get_object_or_404(Course, slug=slug)
   context = {}
   if request.method == 'POST':
        form = ContactCourse(request.POST) # vai receber todos os dados digitado pelo usuario
        if form.is_valid():
            context['is_valid'] = True # apenas envia pra o html que é valido e o html envia a msg que foi enviado com sucesso
            form.send_mail(course) # manda o nome do curso para a def de enviar email
            form = ContactCourse()
   else:
       form = ContactCourse()
   context['form'] = form
   context['course'] = course
   template_name = 'courses/details.html'
   return render(request, template_name, context)

@login_required
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user, course=course
    )
    if created:
        enrollment.active()
        messages.success(request, f'Você foi inscrito no curso [{course}] com sucesso.')
    else:
        messages.info(request, f'Você já está inscrito no curso [{course}].')
    return redirect('accounts:dashboard')