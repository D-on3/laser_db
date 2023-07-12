from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Result
from .forms import ResultForm

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
    return render(request, 'results/result_create.html', {'form': form})

@login_required
def result_list(request):
    results = Result.objects.filter(user=request.user)
    return render(request, 'results/result_list.html', {'results': results})
