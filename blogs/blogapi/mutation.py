
import graphene
from blogapi.models import Post, Comments
from blogapi.schema import CommentsType


class CreatePost(graphene.Mutation):
    id = graphene.Int()
    author = graphene.String()
    title = graphene.String()
    description = graphene.String()

    class Arguments:
        author = graphene.String()
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, author, title, description):
        post = Post(
            author=author,
            title=title,
            description=description,
        )
        post.save()

        return CreatePost(
            id=post.id,
            author=post.author,
            title=post.title,
            description=post.description,
        )


class UpdatePost(graphene.Mutation):
    id = graphene.Int(required=True)
    author = graphene.String(required=True)

    class Arguments:
        id = graphene.Int()
        author = graphene.String()

    def mutate(self, info, id, author):
        post = Post.objects.get(id=id)
        post.author = author
        post.save()

        return UpdatePost(
            id=post.id,
            author=post.author,
        )


class DeletePost(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, **kwargs):
        post = Post.objects.get(pk=kwargs["id"])
        post.delete()
        return DeletePost(ok=True)


class CreateComment(graphene.Mutation):
    author = graphene.String(required=True)
    comment = graphene.String(required=True)
    post_id = graphene.Int(name="post", required=True)

    class Arguments:
        author = graphene.String(required=True)
        comment = graphene.String(required=True)
        post_id = graphene.Int(name="post", required=True)

    comment = graphene.Field(CommentsType)

    def mutate(self, info, author, comment, post_id):
        comment = Comments.objects.create(
            author=author,
            comment=comment,
            post_id=post_id, 
        )
        return CreateComment(comment=comment)


class DeleteComment(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        comment_id = graphene.Int(name="comment")
    
    def mutate(self, info, comment_id):
        comment = Comments.objects.get(id=comment_id)
        comment.delete()
        return DeleteComment(ok=True)


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
    create_comment = CreateComment.Field()
    delete_comment = DeleteComment.Field()