from django.urls import path
from cakeapp.views import SignUpView,SignInView,CategoryCreateView,CakeCreateView,CakeListView,CakeUpdateView,remove_category,remove_cakeView\
,CakeVarientCreateView,CakeDetailView,CakeVarientUpdateView,remove_varient,OfferCreateView,remove_offer,sign_out_view



urlpatterns=[
    path("register/",SignUpView.as_view(),name="signup"),
    path("",SignInView.as_view(),name="signin"),
    path("add/",CategoryCreateView.as_view(),name="category-add"),
    path("categories/<int:pk>/remove/",remove_category,name="remove-category"),
    path("cakes/add",CakeCreateView.as_view(),name="cake-add"),
    path("cakes/all",CakeListView.as_view(),name="cake-list"),
    path("cakes/<int:pk>/change",CakeUpdateView.as_view(),name="cake-change"),
    path("cakes/<int:pk>/remove",remove_cakeView,name="cake-remove"),
    path("cakes/<int:pk>/varients/add",CakeVarientCreateView.as_view(),name="add-varient"),
    path("cakes/<int:pk>/",CakeDetailView.as_view(),name="cake-detail"),
    path("varient/<int:pk>/change/",CakeVarientUpdateView.as_view(),name="update-varient"),
    path("varients/<int:pk>/remove",remove_varient,name="remove-varient"),
    path("varients/<int:pk>/offer/add",OfferCreateView.as_view(),name="offer-add"),
    path("varients/<int:pk>/offers/remove",remove_offer,name="remove-offer"),
    path("logout",sign_out_view,name="signout")






]