from distutils.log import error
from xmlrpc.client import Boolean
from flask_restx import Namespace, Resource, fields

from src.api.v1.commom_api_models import error_model, oids


ns = Namespace(
    "/ca/<commom_name>/",
    description="Certificate Authority Management"
)

@ns.route("/<common_name>/")
class CertificateAuthorityManagement(Resource):

    ca_data = ns.model(
        "ca_data",
        {
            "common_name": fields.String(
                description="Certificate Authority common name",
                example="ca.example.com",
            ),
            "certificate": fields.String(
                description="Certificate",
                example=(
                    "-----BEGIN CERTIFICATE-----"+
                    "R8dXfXcn7qTeMMZE531OoEYgmkUEvlntuRPpSZU6gIy/+PoxS6P5(...)"
                    "-----END CERTIFICATE-----")
            ),
            "intermediate_ca": fields.Boolean(),
            "hash_name": fields.String(),
            "key": fields.String(),
            "public_key": fields.String(),
            "crl": fields.String(),
            "issued_certificates": fields.List(fields.String()),

         }
    )
    common_name_response = ns.model(
        "common_name_response",
        {
            "data": fields.Nested(ca_data),
            "error": fields.Nested(error_model),
        }
    )
    @ns.response(200, "OK", common_name_response)
    def get(self, common_name):
        """Get information of specific Certificate Authority"""
