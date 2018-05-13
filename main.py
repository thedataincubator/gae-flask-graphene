import logging

from flask import Flask
from flask_graphql import GraphQLView
from starwars import schema

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view('graphql_batch', schema=schema, batch=True))

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
