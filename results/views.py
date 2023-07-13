from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Result
from .forms import ResultForm


@login_required
def result_list(request):
    results = Result.objects.filter(user=request.user)
    return render(request, 'results/result_list.html', {'results': results})


@login_required
def result_create(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                'home')  # Redirect to the home page or the desired URL
    else:
        form = ResultForm()

    return render(request, 'results/result_create.html', {'form': form})


@login_required
def result_detail(request, pk):
    result = get_object_or_404(Result, pk=pk)
    return render(request, 'results/result_detail.html', {'result': result})


@login_required
def result_update(request, pk):
    result = get_object_or_404(Result, pk=pk)
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect('result_detail',
                            pk=pk)  # Redirect to the result detail page
    else:
        form = ResultForm(instance=result)

    return render(request, 'results/result_update.html',
                  {'form': form, 'result': result})


@login_required
def result_delete(request, pk):
    result = get_object_or_404(Result, pk=pk)
    if request.method == 'POST':
        result.delete()
        return redirect(
            'home')  # Redirect to the home page or the desired URL

    return render(request, 'results/result_delete.html', {'result': result})
