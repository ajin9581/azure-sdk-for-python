# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class UsageDetailsOperations(object):
    """UsageDetailsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.consumption.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        scope,  # type: str
        expand=None,  # type: Optional[str]
        filter=None,  # type: Optional[str]
        skiptoken=None,  # type: Optional[str]
        top=None,  # type: Optional[int]
        metric=None,  # type: Optional[Union[str, "models.Metrictype"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.UsageDetailsListResult"]
        """Lists the usage details for the defined scope. Usage details are available via this API only
        for May 1, 2014 or later.

        :param scope: The scope associated with usage details operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope,
         '/providers/Microsoft.Billing/departments/{departmentId}' for Department scope,
         '/providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount
         scope and '/providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management
         Group scope. For subscription, billing account, department, enrollment account and management
         group, you can also add billing period to the scope using
         '/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'. For e.g. to specify billing
         period at department scope use
         '/providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'.
         Also, Modern Commerce Account scopes are
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for billingAccount scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners.
        :type scope: str
        :param expand: May be used to expand the properties/additionalInfo or properties/meterDetails
         within a list of usage details. By default, these fields are not included when listing usage
         details.
        :type expand: str
        :param filter: May be used to filter usageDetails by properties/resourceGroup,
         properties/resourceName, properties/resourceId, properties/chargeType,
         properties/reservationId, properties/publisherType or tags. The filter supports 'eq', 'lt',
         'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is
         a key value pair string where key and value is separated by a colon (:). PublisherType Filter
         accepts two values azure and marketplace and it is currently supported for Web Direct Offer
         Type.
        :type filter: str
        :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If
         a previous response contains a nextLink element, the value of the nextLink element will include
         a skiptoken parameter that specifies a starting point to use for subsequent calls.
        :type skiptoken: str
        :param top: May be used to limit the number of results to the most recent N usageDetails.
        :type top: int
        :param metric: Allows to select different type of cost/usage records.
        :type metric: str or ~azure.mgmt.consumption.models.Metrictype
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either UsageDetailsListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.consumption.models.UsageDetailsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.UsageDetailsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if skiptoken is not None:
                    query_parameters['$skiptoken'] = self._serialize.query("skiptoken", skiptoken, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int', maximum=1000, minimum=1)
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if metric is not None:
                    query_parameters['metric'] = self._serialize.query("metric", metric, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('UsageDetailsListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/{scope}/providers/Microsoft.Consumption/usageDetails'}  # type: ignore
