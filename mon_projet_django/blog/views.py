from blog.classes import Post
from django.shortcuts import render

# Create your views here.

# listePost = [
#     {'id': 1, 'title': 'First Post', 'body': 'This is my first post'},
#     {'id': 2, 'title': 'Second Post', 'body': 'This is my second post'},
#     {'id': 3, 'title': 'Third Post', 'body': 'This is my third post'},
# ]

# on change pour utiliser 'listePost' par une classe Post


def index(request):
    liste = Post.listePosts()
    return render(request, 'blog/index.html', {'posts': liste})

def show(request, id):
    post = Post.findPost(id)
    return render(request, 'blog/show.html', {'post': post})