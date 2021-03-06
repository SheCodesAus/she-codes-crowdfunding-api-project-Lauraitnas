from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('comment/', views.CommentListApi.as_view(), name="comment-list"),
    path('category/', views.CategoryList.as_view(), name="category-list"),
    path('comment/<int:pk>/', views.CommentDetailApi.as_view(), name="comment-detail"),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name="category-detail"),
    path('category/<str:slug>/', views.CategoryDetail.as_view(), name="category-detail-slug"),
    path('association/', views.AssociationList.as_view(), name="association-list"),
    path('association/<str:username>/', views.AssociationDetail.as_view(), name="association-detail-username"),


]

urlpatterns = format_suffix_patterns(urlpatterns)