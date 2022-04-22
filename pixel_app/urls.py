from django.urls import path
from pixel_app.views import *

#     path('register/', RegisterView.as_view()),
#     path('login/', LoginView.as_view()),
#     path('credentials/', CredentialsView.as_view())
# ]


urlpatterns = [
    path('pixels/', ListView.as_view()),
    path('pixel/<int:pk>/detail/', DetailView.as_view()),
    path('pixel/<int:pk>/', UpdateDeletePixel.as_view()),
    path('pixel/create/', CreateView.as_view()),

    path('colors/', ListColorView.as_view()),
    path('color/create', CreateColorView.as_view()),
    path('color/<int:pk>', ColorDetailView.as_view()),
    
    path('owners/', ListOwnerView.as_view()),
    path('owners/<int:pk>', DetailOwnerView.as_view()),
    
    
    path('threads/', ListThreadsView.as_view()),
    path('threads/<int:pk>', DetailThreadView.as_view()),
    path('threads/update/<int:pk>', UpdateThreadView.as_view()),
    path('thread/create', CreateThreadView.as_view()),
    
    
    path('comments/', ListCommentView.as_view()),
    path('comments/<int:pk>', DetailCommentView.as_view()),
    path('comments/update/<int:pk>', UpdateCommentView.as_view()),
    path('comment/create', CreateCommentView.as_view()),
    
    path('communities/', ListCommunityView.as_view()),
    path('communities/<int:pk>', DetailCommunityView.as_view()),
    path('communities/update/<int:pk>', UpdateCommunityView.as_view()),
    path('community/create', CreateCommunityView.as_view()),


]