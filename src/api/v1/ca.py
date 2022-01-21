from xmlrpc.client import Boolean
from flask_restx import Namespace, Resource, fields


from src.api.v1.commom_api_models import error_model, oids


ns = Namespace("/ca", description="Certificate Authorities")


@ns.route("")
class CertificateAuthority(Resource):

    certificate_authorities_data = ns.model(
        "certificate_authorities_data",
        {
            "data": fields.Nested(
                ns.model(
                    "certificate_authorities",
                    {
                        "certificate_authorities": fields.List(
                            fields.String(
                               description="Certificate Authority common name",
                                example="ca.example.com",
                            )
                        )
                    }
                )
            ),
            "error": fields.Nested(error_model)
        }
    )
    @ns.response(200, "OK", certificate_authorities_data)
    def get(self):
        """List all Certificate Authorities"""


    certificate_authority_request = ns.model(
        "add_certificate_authority",
        {
            "common_name": fields.String(
                description="Certificate Authority Common Name",
                required=True,
                example="example.com",
            ),
            "dns_names": fields.List(
                fields.String(
                    description="Aditional names",
                    required=True,
                    example="www.example.com",
                )
            ),
            "intermediate": fields.Boolean(
                description="Is it a intermediate Certificate Authority?",
                required=False,
                default=False,
                example=False
            ),
            "oids": fields.Nested(oids),
            "public_exponent": fields.String(
                description="Public Exponent for the Key",
                default=65537,
                example="65537",
            ),
            "key_size": fields.String(
                description="Key size",
                default=2048,
                example="2048",
            ),
        }
    )
    @ns.doc(body=certificate_authority_request, validate=True)
    def post(self):
        """Add new Certificate Authorities"""
