from django.urls import path

from cake_api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("cakes",views.CakeView,basename="cakes")



urlpatterns = [
    path("register/",views.Userview.as_view())
    
]+router.urls
