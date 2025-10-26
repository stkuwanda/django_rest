from django.urls import path
from .views import get_user, create_user

# define urlpatterns for the api app
# these urlpatterns will route requests to the get_user view.
# a view is a function that takes a web request and returns a web response. In NodeJs views are called controllers.
urlpatterns = [
  path('users/', get_user, name='get_user'), # route to get_user view
  path('users/create', create_user, name='create_user') # route to create_user view
] 