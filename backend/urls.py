from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('auth_user.urls')),
    path('api/home/', include('home.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# {
#     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0NjA2NjQ2LCJpYXQiOjE3MTQ1NzY2NDYsImp0aSI6IjUwNmE0OGNkNDdhYTRlNmU5YWQ1N2ZlZmZkYzdhOWZjIiwidXNlcl9pZCI6Mn0.CLhr3WyZhCG_iPlmF8-3HJpWK6726KJaFYNPxNSO2jw",
#     "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNDYxODY0NiwiaWF0IjoxNzE0NTc2NjQ2LCJqdGkiOiJlOWFmNjA3Y2YzOWY0NGU2OTljMmEzNTY2ODQ4MzE2OCIsInVzZXJfaWQiOjJ9.Flc6XOzBxghStGXn8gGJ4hqWILvgv95M8Pfc8Xy-AF8"
# }