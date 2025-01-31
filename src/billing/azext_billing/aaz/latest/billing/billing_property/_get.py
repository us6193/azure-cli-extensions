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
    "billing billing-property get",
)
class Get(AAZCommand):
    """Get the billing properties for a subscription

    :example: BillingPropertyGetMCA
        az billing billing-property get
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.billing/billingproperty/default", "2024-04-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.include_billing_country = AAZBoolArg(
            options=["--include-billing-country"],
            help="A flag that specifies whether or not to include billing country.",
            default=False,
        )
        _args_schema.include_transition_status = AAZBoolArg(
            options=["--include-transition-status"],
            help="A flag that specifies whether or not to include transition status for billing accounts with agreement type Microsoft Customer Agreement.",
            default=False,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.BillingPropertyGet(ctx=self.ctx)()
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

    class BillingPropertyGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Billing/billingProperty/default",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "includeBillingCountry", self.ctx.args.include_billing_country,
                ),
                **self.serialize_query_param(
                    "includeTransitionStatus", self.ctx.args.include_transition_status,
                ),
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
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.account_admin_notification_email_address = AAZStrType(
                serialized_name="accountAdminNotificationEmailAddress",
                flags={"read_only": True},
            )
            properties.billing_account_agreement_type = AAZStrType(
                serialized_name="billingAccountAgreementType",
                flags={"read_only": True},
            )
            properties.billing_account_display_name = AAZStrType(
                serialized_name="billingAccountDisplayName",
                flags={"read_only": True},
            )
            properties.billing_account_id = AAZStrType(
                serialized_name="billingAccountId",
                flags={"read_only": True},
            )
            properties.billing_account_sold_to_country = AAZStrType(
                serialized_name="billingAccountSoldToCountry",
                flags={"read_only": True},
            )
            properties.billing_account_status = AAZStrType(
                serialized_name="billingAccountStatus",
                flags={"read_only": True},
            )
            properties.billing_account_status_reason_code = AAZStrType(
                serialized_name="billingAccountStatusReasonCode",
                flags={"read_only": True},
            )
            properties.billing_account_sub_type = AAZStrType(
                serialized_name="billingAccountSubType",
                flags={"read_only": True},
            )
            properties.billing_account_type = AAZStrType(
                serialized_name="billingAccountType",
                flags={"read_only": True},
            )
            properties.billing_currency = AAZStrType(
                serialized_name="billingCurrency",
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
            properties.billing_profile_payment_method_family = AAZStrType(
                serialized_name="billingProfilePaymentMethodFamily",
                flags={"read_only": True},
            )
            properties.billing_profile_payment_method_type = AAZStrType(
                serialized_name="billingProfilePaymentMethodType",
                flags={"read_only": True},
            )
            properties.billing_profile_spending_limit = AAZStrType(
                serialized_name="billingProfileSpendingLimit",
                flags={"read_only": True},
            )
            properties.billing_profile_spending_limit_details = AAZListType(
                serialized_name="billingProfileSpendingLimitDetails",
                flags={"read_only": True},
            )
            properties.billing_profile_status = AAZStrType(
                serialized_name="billingProfileStatus",
                flags={"read_only": True},
            )
            properties.billing_profile_status_reason_code = AAZStrType(
                serialized_name="billingProfileStatusReasonCode",
                flags={"read_only": True},
            )
            properties.billing_tenant_id = AAZStrType(
                serialized_name="billingTenantId",
                flags={"read_only": True},
            )
            properties.cost_center = AAZStrType(
                serialized_name="costCenter",
            )
            properties.customer_display_name = AAZStrType(
                serialized_name="customerDisplayName",
                flags={"read_only": True},
            )
            properties.customer_id = AAZStrType(
                serialized_name="customerId",
                flags={"read_only": True},
            )
            properties.customer_status = AAZStrType(
                serialized_name="customerStatus",
                flags={"read_only": True},
            )
            properties.enrollment_details = AAZObjectType(
                serialized_name="enrollmentDetails",
            )
            properties.invoice_section_display_name = AAZStrType(
                serialized_name="invoiceSectionDisplayName",
                flags={"read_only": True},
            )
            properties.invoice_section_id = AAZStrType(
                serialized_name="invoiceSectionId",
                flags={"read_only": True},
            )
            properties.invoice_section_status = AAZStrType(
                serialized_name="invoiceSectionStatus",
                flags={"read_only": True},
            )
            properties.invoice_section_status_reason_code = AAZStrType(
                serialized_name="invoiceSectionStatusReasonCode",
                flags={"read_only": True},
            )
            properties.is_account_admin = AAZBoolType(
                serialized_name="isAccountAdmin",
                flags={"read_only": True},
            )
            properties.is_transitioned_billing_account = AAZBoolType(
                serialized_name="isTransitionedBillingAccount",
                flags={"read_only": True},
            )
            properties.product_id = AAZStrType(
                serialized_name="productId",
                flags={"read_only": True},
            )
            properties.product_name = AAZStrType(
                serialized_name="productName",
                flags={"read_only": True},
            )
            properties.sku_description = AAZStrType(
                serialized_name="skuDescription",
                flags={"read_only": True},
            )
            properties.sku_id = AAZStrType(
                serialized_name="skuId",
                flags={"read_only": True},
            )
            properties.subscription_billing_status = AAZStrType(
                serialized_name="subscriptionBillingStatus",
                flags={"read_only": True},
            )
            properties.subscription_billing_status_details = AAZListType(
                serialized_name="subscriptionBillingStatusDetails",
                flags={"read_only": True},
            )
            properties.subscription_billing_type = AAZStrType(
                serialized_name="subscriptionBillingType",
                flags={"read_only": True},
            )
            properties.subscription_service_usage_address = AAZObjectType(
                serialized_name="subscriptionServiceUsageAddress",
            )
            properties.subscription_workload_type = AAZStrType(
                serialized_name="subscriptionWorkloadType",
                flags={"read_only": True},
            )

            billing_profile_spending_limit_details = cls._schema_on_200.properties.billing_profile_spending_limit_details
            billing_profile_spending_limit_details.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.billing_profile_spending_limit_details.Element
            _element.amount = AAZFloatType()
            _element.currency = AAZStrType()
            _element.end_date = AAZStrType(
                serialized_name="endDate",
            )
            _element.start_date = AAZStrType(
                serialized_name="startDate",
            )
            _element.status = AAZStrType()
            _element.type = AAZStrType()

            enrollment_details = cls._schema_on_200.properties.enrollment_details
            enrollment_details.department_display_name = AAZStrType(
                serialized_name="departmentDisplayName",
            )
            enrollment_details.department_id = AAZStrType(
                serialized_name="departmentId",
            )
            enrollment_details.enrollment_account_display_name = AAZStrType(
                serialized_name="enrollmentAccountDisplayName",
            )
            enrollment_details.enrollment_account_id = AAZStrType(
                serialized_name="enrollmentAccountId",
            )
            enrollment_details.enrollment_account_status = AAZStrType(
                serialized_name="enrollmentAccountStatus",
            )

            subscription_billing_status_details = cls._schema_on_200.properties.subscription_billing_status_details
            subscription_billing_status_details.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.subscription_billing_status_details.Element
            _element.effective_date = AAZStrType(
                serialized_name="effectiveDate",
                flags={"read_only": True},
            )
            _element.reason = AAZStrType(
                flags={"read_only": True},
            )

            subscription_service_usage_address = cls._schema_on_200.properties.subscription_service_usage_address
            subscription_service_usage_address.address_line1 = AAZStrType(
                serialized_name="addressLine1",
                flags={"required": True},
            )
            subscription_service_usage_address.address_line2 = AAZStrType(
                serialized_name="addressLine2",
            )
            subscription_service_usage_address.address_line3 = AAZStrType(
                serialized_name="addressLine3",
            )
            subscription_service_usage_address.city = AAZStrType()
            subscription_service_usage_address.company_name = AAZStrType(
                serialized_name="companyName",
            )
            subscription_service_usage_address.country = AAZStrType(
                flags={"required": True},
            )
            subscription_service_usage_address.district = AAZStrType()
            subscription_service_usage_address.email = AAZStrType()
            subscription_service_usage_address.first_name = AAZStrType(
                serialized_name="firstName",
            )
            subscription_service_usage_address.is_valid_address = AAZBoolType(
                serialized_name="isValidAddress",
            )
            subscription_service_usage_address.last_name = AAZStrType(
                serialized_name="lastName",
            )
            subscription_service_usage_address.middle_name = AAZStrType(
                serialized_name="middleName",
            )
            subscription_service_usage_address.phone_number = AAZStrType(
                serialized_name="phoneNumber",
            )
            subscription_service_usage_address.postal_code = AAZStrType(
                serialized_name="postalCode",
            )
            subscription_service_usage_address.region = AAZStrType()

            system_data = cls._schema_on_200.system_data
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

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _GetHelper:
    """Helper class for Get"""


__all__ = ["Get"]
