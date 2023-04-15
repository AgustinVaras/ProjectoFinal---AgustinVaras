from django.urls import path
from core.views import inicio, PostAddView, PostDetailView, PostsListarView, PostEditView, PostDeleteView,CategAddView

urlpatterns = [
    path("", inicio, name="home"),
    
    #List Views
    path("List_Posts", PostsListarView.as_view(), name="List_Posts"),

    #Add Views
    path("add_post", PostAddView.as_view(), name="Add_Post"),
    path("Categoria/add/", CategAddView.as_view(), name="Add_Categoria"),
    
    #Detail Views
    path("post/<int:pk>", PostDetailView.as_view(), name="Detail_Post"),
    
    #Edit Views
    path("post/edit/<int:pk>", PostEditView.as_view(), name="Edit_Post"),

    #Delete Views
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="Delete_Post" ),
]
