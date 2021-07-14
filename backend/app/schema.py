import graphene

import project_requests.schema
import tasks.schema

# Schema app


class Query(project_requests.schema.Query, tasks.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
