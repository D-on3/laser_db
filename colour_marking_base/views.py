from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Author, Machine, Result
from .forms import ResultForm

@login_required
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

@login_required
def machine_list(request):
    machines = Machine.objects.all()
    return render(request, 'machine_list.html', {'machines': machines})

@login_required
def result_list(request):
    results = Result.objects.filter(user=request.user)
    return render(request, 'result_list.html', {'results': results})

@login_required
def result_create(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.user = request.user
            result.save()
            return redirect('result_list')
    else:
        form = ResultForm()
    return render(request, 'result_form.html', {'form': form})

@login_required
def result_detail(request, result_id):
    result = Result.objects.get(id=result_id)
    return render(request, 'result_details.html', {'result': result})

@login_required
def result_update(request, result_id):
    result = Result.objects.get(id=result_id)
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect('result_list')
    else:
        form = ResultForm(instance=result)
    return render(request, 'result_form.html', {'form': form})
