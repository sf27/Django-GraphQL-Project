import graphene

import base_app.schema


class Query(base_app.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


Query.name = "Test Project"

schema = graphene.Schema(query=Query)
