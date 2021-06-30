import graphene

import project_requests.schema

# Schema app


class Query(project_requests.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
