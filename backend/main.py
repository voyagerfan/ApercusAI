from fastapi import FastApi
import strawberry
from strawberry.fastapi import GraphQLRouter


def create_app():

    graphql_router = GraphQLRouter() #TODO: Add a schema

    app = FastApi(
        title="ApercusAI",
        description="""
        ApercusAI API allows for the receipt of data, analysis and transmission of insights.

        ## Items
        You can POST the excel or csv data.

        ## Users

        You will be able to:
        * Upload your data
        * Configure your desired analysis
        * Have the data sent back in a digestable format

        """,
        version="0.0.1"
    ).include_router(graphql_router, prefix="/graphql")

    return app

app = create_app