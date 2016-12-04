from django.conf.urls import url

from api.loginsys import Login, Logout, Registration
from api.profile import UserProfile
from api.post import UserPost


urlpatterns = [
    url(r'login/$', Login.as_view()),
    url(r'logout/$', Logout.as_view()),
    url(r'registration/$', Registration.as_view()),
    url(r'profile/$', UserProfile.as_view()),
    url(r'post/$', UserPost.as_view())
]
