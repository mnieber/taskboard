import graphene

import project_requests.schema
import tasks.schema


class Query(project_requests.schema.Query, tasks.schema.Query, graphene.ObjectType):
    pass


class Mutation(
    project_requests.schema.Mutation, tasks.schema.Mutation, graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
