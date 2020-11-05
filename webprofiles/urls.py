from django.contrib import admin
from django.urls import path, include
from webprofiles import views
from rest_framework import routers
from webprofiles.views import EmployeeView, EmployeeUpdate

# router = routers.SimpleRouter()
# router.register(r'create-view', EmployeeView)
# router.register(r'update-delete/<int:pk>', EmployeeUpdate)
# urlpatterns = router.urls

urlpatterns = [
    path('create/',views.EmployeeView.as_view()),
    path('update/<int:pk>', views.EmployeeUpdate.as_view()),
    # path('', include(router.urls)),

]