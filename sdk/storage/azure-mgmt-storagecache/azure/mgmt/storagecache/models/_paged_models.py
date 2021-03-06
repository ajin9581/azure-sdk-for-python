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

from msrest.paging import Paged


class ApiOperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ApiOperation <azure.mgmt.storagecache.models.ApiOperation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ApiOperation]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApiOperationPaged, self).__init__(*args, **kwargs)
class ResourceSkuPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ResourceSku <azure.mgmt.storagecache.models.ResourceSku>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ResourceSku]'}
    }

    def __init__(self, *args, **kwargs):

        super(ResourceSkuPaged, self).__init__(*args, **kwargs)
class UsageModelPaged(Paged):
    """
    A paging container for iterating over a list of :class:`UsageModel <azure.mgmt.storagecache.models.UsageModel>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[UsageModel]'}
    }

    def __init__(self, *args, **kwargs):

        super(UsageModelPaged, self).__init__(*args, **kwargs)
class CachePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Cache <azure.mgmt.storagecache.models.Cache>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Cache]'}
    }

    def __init__(self, *args, **kwargs):

        super(CachePaged, self).__init__(*args, **kwargs)
class StorageTargetPaged(Paged):
    """
    A paging container for iterating over a list of :class:`StorageTarget <azure.mgmt.storagecache.models.StorageTarget>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StorageTarget]'}
    }

    def __init__(self, *args, **kwargs):

        super(StorageTargetPaged, self).__init__(*args, **kwargs)
