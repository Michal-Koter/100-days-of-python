class User:
    def __init__(self, name, is_logged_in=False):
        self.name = name
        self.is_logged_in = is_logged_in


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def creat_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Adam")
creat_blog_post(new_user)

logged_user = User("Jack", True)
creat_blog_post(logged_user)