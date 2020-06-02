# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AzureResourceProperties
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import LogAnalyticsQueryPack
    from ._models_py3 import LogAnalyticsQueryPackQuery
    from ._models_py3 import LogAnalyticsQueryPackQuerySearchProperties
    from ._models_py3 import QueryPacksResource
    from ._models_py3 import TagsResource
except (SyntaxError, ImportError):
    from ._models import AzureResourceProperties
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import LogAnalyticsQueryPack
    from ._models import LogAnalyticsQueryPackQuery
    from ._models import LogAnalyticsQueryPackQuerySearchProperties
    from ._models import QueryPacksResource
    from ._models import TagsResource
from ._paged_models import LogAnalyticsQueryPackPaged
from ._paged_models import LogAnalyticsQueryPackQueryPaged

__all__ = [
    'AzureResourceProperties',
    'ErrorResponse', 'ErrorResponseException',
    'LogAnalyticsQueryPack',
    'LogAnalyticsQueryPackQuery',
    'LogAnalyticsQueryPackQuerySearchProperties',
    'QueryPacksResource',
    'TagsResource',
    'LogAnalyticsQueryPackQueryPaged',
    'LogAnalyticsQueryPackPaged',
]