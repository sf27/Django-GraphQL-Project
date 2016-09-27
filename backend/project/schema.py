import graphene

import base_app.schema


class Category(graphene.ObjectType):
    name = graphene.String()


class CategoryCreateMutation(graphene.ObjectType):
    create_category = graphene.Field(base_app.schema.CreateCategory)
    category = graphene.Field(Category)


class Query(base_app.schema.Query):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(
    name='Project Schema',
    mutation=CategoryCreateMutation,
)
schema.query = Query
