import graphene
from graphene_django import DjangoObjectType
from .models import Post, Comments


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class CommentsType(DjangoObjectType):
    class Meta:
        model = Comments


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    post_id = graphene.Field(PostType, id=graphene.Int())
    detail_post_id = graphene.List(PostType, id=graphene.Int())

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_post_id(self, info, id):
        return Post.objects.get(id=id)
    
    def resolve_detail_post_id(self, info, id):
        return Post.objects.get(id=id).comments_set.all()
