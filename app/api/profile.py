from django.views.generic import View
from django.http import JsonResponse

from api.utils import error_resp
from api.models import Key, Post


class UserProfile(View):
    def get(self, request):
        key = request.GET.get('key', None)
        if key is None:
            return error_resp(
                422,
                'Unacceptable',
                'API key is missing'
            )
        key_filter = Key.objects.filter(key=key)
        if not key_filter:
            return error_resp(
                412, 'Precondition Failed', 'API key is invalid'
            )
        key = key_filter[0]
        user = key.user
        posts = Post.objects.filter(user=user)
        return JsonResponse(
            {'username': user.username,
             'email': user.email,
             'posts_count': len(posts)}
        )
