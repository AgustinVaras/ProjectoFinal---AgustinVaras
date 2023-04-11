from django.urls import path
from core.views import inicio, login_form, PostAddView, PostDetailView, PostsListarView

urlpatterns = [
    path("", inicio, name="index.html"),
    path("login", login_form, name="login"),
    
    #List Views
    path("List_Posts", PostsListarView.as_view(), name="List_Posts"),

    #Add Views
    path("add_post", PostAddView.as_view(), name="Add_Post"),
    
    #Detail Views
    path("post/<post_name>", PostDetailView.as_view(), name="Detail_Post"),
    
]
