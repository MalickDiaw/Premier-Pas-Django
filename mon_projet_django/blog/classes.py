from django.http import Http404


class Post():

    listePost = [
        {'id': 1, 'title': 'First Post', 'body': 'This is my first post'},
        {'id': 2, 'title': 'Second Post', 'body': 'This is my second post'},
        {'id': 3, 'title': 'Third Post', 'body': 'This is my third post'},
    ]

    @classmethod
    def listePosts(cls):
        return cls.listePost

    @classmethod
    def findPost(cls, id):
        try:
            return cls.listePost[id - 1]
        except:
            raise Http404("Post #{} n'existe pas".format(id))
