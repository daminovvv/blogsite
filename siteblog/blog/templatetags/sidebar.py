from django import template
from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular(cnt=3):
    popular_posts = Post.objects.order_by('-views')[:cnt]
    return {"popular_posts": popular_posts}


@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()[:25]
    return {"tags": tags}