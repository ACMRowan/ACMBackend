from django.http import JsonResponse

from .models import Announcement

def announcements(request):
	announcements = Announcement.objects.all().values()
	return JsonResponse(list(announcements), safe=False)

