from flask_restx import Api

from src import app, __version__
from src.api.v1.ca import ns as ca_v1
from src.api.v1.ca_management import ns as ca_management_v1
from src.api.v1.commom_api_models import api_models_namespace

api = Api(
    app,
    version=__version__.version,
    title="OwnCA REST API",
    description="OwnCA REST API",
)

api.add_namespace(api_models_namespace)
api.add_namespace(ca_v1, path="/api/v1/ca")
api.add_namespace(ca_management_v1, path="/api/v1/ca")
