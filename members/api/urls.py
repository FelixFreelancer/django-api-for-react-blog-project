from django.urls import path

# custom import
from .views import (
MemberDetailView, MembersListView, MemberCreateView, MemberUpdateView, MemberDeleteView
)
urlpatterns = [
    path('', MembersListView.as_view()),
    path('create', MemberCreateView.as_view()),
    path('update/<pk>', MemberUpdateView.as_view()),
    path('delete/<pk>', MemberDeleteView.as_view()),
    path('<pk>', MemberDetailView.as_view())
]