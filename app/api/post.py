import json

from django.views.generic import View
from django.http import JsonResponse

from api.utils import error_resp, custom_paginator
from api.models import Key, Post


class UserPost(View):
    def post(self, request):
        request_as_json = json.loads(request.body.decode('utf-8'))
        title = request_as_json.get('title', None)
        key = request_as_json.get('key', None)
        body = request_as_json.get('body', None)
        if title is None or body is None or key is None:
            return error_resp(
                422,
                'Unacceptable',
                'Body parameters must be title, body and API key'
            )

        key_filter = Key.objects.filter(key=key)
        if not key_filter:
            return error_resp(
                412, 'Precondition Failed', 'API key is invalid'
            )
        if len(title) > 100:
            return error_resp(
                422, 'Unacceptable', 'Longer title, required less 100 symbols')
        key = key_filter[0]
        user = key.user
        post = Post.objects.create(user=user, title=title, body=body)
        post.save()
        return JsonResponse({'message': 'Post successful'})

    def get(self, request):
        key = request.GET.get('key', None)
        if key is None:
            return error_resp(
                422,
                'Unacceptable',
                'API key is missing'
            )
        key_filter = Key.objects.filter(key=key)
        key = key_filter[0]
        if not key_filter:
            return error_resp(
                412, 'Precondition Failed', 'API key is invalid'
            )

        query_args = {}
        title = request.GET.get('title', None)
        if title is not None:
            title = ' '.join(title.split('+'))
            query_args.update({'title__contains': title})

        body = request.GET.get('body', None)
        if body is not None:
            body = ' '.join(body.split('+'))
            query_args.update({'body__contains': body})
        is_all_posts = request.GET.get('all', None)
        if is_all_posts is None:
            query_args.update({'user': key.user})

        posts = self._get_posts(query_args)

        page = request.GET.get('page', None)
        if page is None:
            return JsonResponse(posts, safe=False)
        else:
            return custom_paginator(posts, page)

    @staticmethod
    def _get_posts(query_args):
        posts = Post.objects.filter(**query_args)
        return list(map(
            lambda post: {'title': post.title, 'body': post.body}, posts))
