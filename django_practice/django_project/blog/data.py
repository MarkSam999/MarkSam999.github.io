# Use it before changing the data
from blog.models import Post
from django.contrib.auth.models import User

post_1 = Post(title='Blog 1', content='First Post Content!', author=user)
post_1.save()
post_2 = Post(title='Blog 2', content='Second Post Content', author_id=user.id)
post_2.save()
# Type it to watch the data
Post.objects.all()