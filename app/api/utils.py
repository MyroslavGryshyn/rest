from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def error_resp(code, error_type, message):
    """A helper function error request.
    :param code: appropriate error code
    :param error_type: appropriate error type
    :param message: a short description of the error
    :return: Returns a JsonResponse object with information concerning the error
     - error code, error type and error message.
    """
    return JsonResponse(
        {'error':
            {
                'code': code,
                'type': error_type,
                'message': message,
            }
        },
        status=code
    )


def custom_paginator(posts, page, contants=4):
    paginator = Paginator(posts, contants)
    try:
        contant = paginator.page(page)
    except EmptyPage:
        contant = paginator.page(paginator.num_pages)
    return JsonResponse(list(contant), safe=False)
