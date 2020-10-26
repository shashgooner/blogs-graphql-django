import graphene
import blogapi.schema
import blogapi.mutation


class Query(blogapi.schema.Query, graphene.ObjectType):
    pass


class Mutation(blogapi.mutation.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)