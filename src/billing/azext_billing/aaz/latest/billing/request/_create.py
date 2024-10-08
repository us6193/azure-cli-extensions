# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "billing request create",
)
class Create(AAZCommand):
    """Create a billing request.

    :example: BillingRequestsCreateOrUpdate
        az billing request create --billing-request-name 00000000-0000-0000-0000-000000000000 --additional-information "{RoleId:40000000-aaaa-bbbb-cccc-200000000006}" --decision-reason New team member --request-scope /providers/Microsoft.Billing/billingAccounts/00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000_2019-05-31/billingProfiles/xxxx-xxxx-xxx-xxx --status Pending --type RoleAssignment
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingrequests/{}", "2024-04-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.billing_request_name = AAZStrArg(
            options=["--billing-request-name"],
            help="The ID that uniquely identifies a billing request.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$",
            ),
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \\ ? /",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.additional_information = AAZDictArg(
            options=["--additional-information"],
            arg_group="Properties",
            help="Additional information for the billing request.",
        )
        _args_schema.created_by = AAZObjectArg(
            options=["--created-by"],
            arg_group="Properties",
            help="The principal of the entity who created the request.",
        )
        _args_schema.decision_reason = AAZStrArg(
            options=["--decision-reason"],
            arg_group="Properties",
            help="The reason to approve or decline the request.",
        )
        _args_schema.justification = AAZStrArg(
            options=["--justification"],
            arg_group="Properties",
            help="Justification for submitting request.",
        )
        _args_schema.last_updated_by = AAZObjectArg(
            options=["--last-updated-by"],
            arg_group="Properties",
            help="The principal of the entity who last updated the request.",
        )
        _args_schema.recipients = AAZListArg(
            options=["--recipients"],
            arg_group="Properties",
            help="The recipients of the billing request.",
        )
        _args_schema.request_scope = AAZStrArg(
            options=["--request-scope"],
            arg_group="Properties",
            help="The billing scope for which the request was submitted (ex. '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}').",
        )
        _args_schema.reviewed_by = AAZObjectArg(
            options=["--reviewed-by"],
            arg_group="Properties",
            help="The principal of the request reviewer. Will only be set if request is approved.",
        )
        _args_schema.status = AAZStrArg(
            options=["--status"],
            arg_group="Properties",
            help="Status of billing request.",
            enum={"Approved": "Approved", "Cancelled": "Cancelled", "Completed": "Completed", "Declined": "Declined", "Expired": "Expired", "Other": "Other", "Pending": "Pending"},
        )
        _args_schema.type = AAZStrArg(
            options=["--type"],
            arg_group="Properties",
            help="Type of billing request.",
            enum={"InvoiceAccess": "InvoiceAccess", "Other": "Other", "ProvisioningAccess": "ProvisioningAccess", "RoleAssignment": "RoleAssignment", "UpdateBillingPolicy": "UpdateBillingPolicy"},
        )

        additional_information = cls._args_schema.additional_information
        additional_information.Element = AAZStrArg()

        created_by = cls._args_schema.created_by
        created_by.object_id = AAZStrArg(
            options=["object-id"],
            help="The object id of the principal who has interacted with a billing entity.",
        )
        created_by.tenant_id = AAZStrArg(
            options=["tenant-id"],
            help="The tenant id of the principal who has interacted with a billing entity.",
        )
        created_by.upn = AAZStrArg(
            options=["upn"],
            help="The user principal name of the principal who has interacted with a billing entity.",
        )

        last_updated_by = cls._args_schema.last_updated_by
        last_updated_by.object_id = AAZStrArg(
            options=["object-id"],
            help="The object id of the principal who has interacted with a billing entity.",
        )
        last_updated_by.tenant_id = AAZStrArg(
            options=["tenant-id"],
            help="The tenant id of the principal who has interacted with a billing entity.",
        )
        last_updated_by.upn = AAZStrArg(
            options=["upn"],
            help="The user principal name of the principal who has interacted with a billing entity.",
        )

        recipients = cls._args_schema.recipients
        recipients.Element = AAZObjectArg()

        _element = cls._args_schema.recipients.Element
        _element.object_id = AAZStrArg(
            options=["object-id"],
            help="The object id of the principal who has interacted with a billing entity.",
        )
        _element.tenant_id = AAZStrArg(
            options=["tenant-id"],
            help="The tenant id of the principal who has interacted with a billing entity.",
        )
        _element.upn = AAZStrArg(
            options=["upn"],
            help="The user principal name of the principal who has interacted with a billing entity.",
        )

        reviewed_by = cls._args_schema.reviewed_by
        reviewed_by.object_id = AAZStrArg(
            options=["object-id"],
            help="The object id of the principal who has interacted with a billing entity.",
        )
        reviewed_by.tenant_id = AAZStrArg(
            options=["tenant-id"],
            help="The tenant id of the principal who has interacted with a billing entity.",
        )
        reviewed_by.upn = AAZStrArg(
            options=["upn"],
            help="The user principal name of the principal who has interacted with a billing entity.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.BillingRequestsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class BillingRequestsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Billing/billingRequests/{billingRequestName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "billingRequestName", self.ctx.args.billing_request_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-04-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType)
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("additionalInformation", AAZDictType, ".additional_information")
                properties.set_prop("createdBy", AAZObjectType, ".created_by")
                properties.set_prop("decisionReason", AAZStrType, ".decision_reason")
                properties.set_prop("justification", AAZStrType, ".justification")
                properties.set_prop("lastUpdatedBy", AAZObjectType, ".last_updated_by")
                properties.set_prop("recipients", AAZListType, ".recipients")
                properties.set_prop("requestScope", AAZStrType, ".request_scope")
                properties.set_prop("reviewedBy", AAZObjectType, ".reviewed_by")
                properties.set_prop("status", AAZStrType, ".status")
                properties.set_prop("type", AAZStrType, ".type")

            additional_information = _builder.get(".properties.additionalInformation")
            if additional_information is not None:
                additional_information.set_elements(AAZStrType, ".")

            created_by = _builder.get(".properties.createdBy")
            if created_by is not None:
                created_by.set_prop("objectId", AAZStrType, ".object_id")
                created_by.set_prop("tenantId", AAZStrType, ".tenant_id")
                created_by.set_prop("upn", AAZStrType, ".upn")

            last_updated_by = _builder.get(".properties.lastUpdatedBy")
            if last_updated_by is not None:
                last_updated_by.set_prop("objectId", AAZStrType, ".object_id")
                last_updated_by.set_prop("tenantId", AAZStrType, ".tenant_id")
                last_updated_by.set_prop("upn", AAZStrType, ".upn")

            recipients = _builder.get(".properties.recipients")
            if recipients is not None:
                recipients.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.recipients[]")
            if _elements is not None:
                _elements.set_prop("objectId", AAZStrType, ".object_id")
                _elements.set_prop("tenantId", AAZStrType, ".tenant_id")
                _elements.set_prop("upn", AAZStrType, ".upn")

            reviewed_by = _builder.get(".properties.reviewedBy")
            if reviewed_by is not None:
                reviewed_by.set_prop("objectId", AAZStrType, ".object_id")
                reviewed_by.set_prop("tenantId", AAZStrType, ".tenant_id")
                reviewed_by.set_prop("upn", AAZStrType, ".upn")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType()
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.additional_information = AAZDictType(
                serialized_name="additionalInformation",
            )
            properties.billing_account_display_name = AAZStrType(
                serialized_name="billingAccountDisplayName",
                flags={"read_only": True},
            )
            properties.billing_account_id = AAZStrType(
                serialized_name="billingAccountId",
                flags={"read_only": True},
            )
            properties.billing_account_name = AAZStrType(
                serialized_name="billingAccountName",
                flags={"read_only": True},
            )
            properties.billing_account_primary_billing_tenant_id = AAZStrType(
                serialized_name="billingAccountPrimaryBillingTenantId",
                flags={"read_only": True},
            )
            properties.billing_profile_display_name = AAZStrType(
                serialized_name="billingProfileDisplayName",
                flags={"read_only": True},
            )
            properties.billing_profile_id = AAZStrType(
                serialized_name="billingProfileId",
                flags={"read_only": True},
            )
            properties.billing_profile_name = AAZStrType(
                serialized_name="billingProfileName",
                flags={"read_only": True},
            )
            properties.billing_scope = AAZStrType(
                serialized_name="billingScope",
                flags={"read_only": True},
            )
            properties.created_by = AAZObjectType(
                serialized_name="createdBy",
            )
            properties.creation_date = AAZStrType(
                serialized_name="creationDate",
                flags={"read_only": True},
            )
            properties.customer_display_name = AAZStrType(
                serialized_name="customerDisplayName",
                flags={"read_only": True},
            )
            properties.customer_id = AAZStrType(
                serialized_name="customerId",
                flags={"read_only": True},
            )
            properties.customer_name = AAZStrType(
                serialized_name="customerName",
                flags={"read_only": True},
            )
            properties.decision_reason = AAZStrType(
                serialized_name="decisionReason",
            )
            properties.expiration_date = AAZStrType(
                serialized_name="expirationDate",
                flags={"read_only": True},
            )
            properties.invoice_section_display_name = AAZStrType(
                serialized_name="invoiceSectionDisplayName",
                flags={"read_only": True},
            )
            properties.invoice_section_id = AAZStrType(
                serialized_name="invoiceSectionId",
                flags={"read_only": True},
            )
            properties.invoice_section_name = AAZStrType(
                serialized_name="invoiceSectionName",
                flags={"read_only": True},
            )
            properties.justification = AAZStrType()
            properties.last_updated_by = AAZObjectType(
                serialized_name="lastUpdatedBy",
            )
            properties.last_updated_date = AAZStrType(
                serialized_name="lastUpdatedDate",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.recipients = AAZListType()
            properties.request_scope = AAZStrType(
                serialized_name="requestScope",
            )
            properties.reviewal_date = AAZStrType(
                serialized_name="reviewalDate",
                flags={"read_only": True},
            )
            properties.reviewed_by = AAZObjectType(
                serialized_name="reviewedBy",
            )
            properties.status = AAZStrType()
            properties.subscription_display_name = AAZStrType(
                serialized_name="subscriptionDisplayName",
                flags={"read_only": True},
            )
            properties.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
                flags={"read_only": True},
            )
            properties.subscription_name = AAZStrType(
                serialized_name="subscriptionName",
                flags={"read_only": True},
            )
            properties.type = AAZStrType()

            additional_information = cls._schema_on_200_201.properties.additional_information
            additional_information.Element = AAZStrType()

            created_by = cls._schema_on_200_201.properties.created_by
            created_by.object_id = AAZStrType(
                serialized_name="objectId",
            )
            created_by.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )
            created_by.upn = AAZStrType()

            last_updated_by = cls._schema_on_200_201.properties.last_updated_by
            last_updated_by.object_id = AAZStrType(
                serialized_name="objectId",
            )
            last_updated_by.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )
            last_updated_by.upn = AAZStrType()

            recipients = cls._schema_on_200_201.properties.recipients
            recipients.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.recipients.Element
            _element.object_id = AAZStrType(
                serialized_name="objectId",
            )
            _element.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )
            _element.upn = AAZStrType()

            reviewed_by = cls._schema_on_200_201.properties.reviewed_by
            reviewed_by.object_id = AAZStrType(
                serialized_name="objectId",
            )
            reviewed_by.tenant_id = AAZStrType(
                serialized_name="tenantId",
            )
            reviewed_by.upn = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
