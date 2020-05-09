import graphene
# import users.schema
import musicapp.schema


class Query(musicapp.schema.Query, graphene.ObjectType):
    pass


# Runs mutation function from music app
# class Mutation(users.schema.Mutation, musicapp.schema.Mutation, graphene.ObjectType,):
#     pass

# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query)
