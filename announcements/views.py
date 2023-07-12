from django.shortcuts import render, get_object_or_404
from .models import Announcement

def announcement_list_view(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements})

def announcement_detail_view(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    return render(request, 'announcements/announcement_detail.html', {'announcement': announcement})
