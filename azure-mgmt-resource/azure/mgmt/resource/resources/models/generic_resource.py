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

from .resource_model import ResourceModel


class GenericResource(ResourceModel):
    """Resource information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param plan: The plan of the resource.
    :type plan: :class:`Plan <azure.mgmt.resource.resources.models.Plan>`
    :param properties: The resource properties.
    :type properties: object
    :param kind: The kind of the resource.
    :type kind: str
    :param managed_by: Id of the resource that manages this resource.
    :type managed_by: str
    :param sku: The sku of the resource.
    :type sku: :class:`Sku <azure.mgmt.resource.resources.models.Sku>`
    :param identity: The identity of the resource.
    :type identity: :class:`Identity
     <azure.mgmt.resource.resources.models.Identity>`
    """ 

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'kind': {'pattern': '^[-\w\._,\(\)]+$'},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'properties': {'key': 'properties', 'type': 'object'},
        'kind': {'key': 'kind', 'type': 'str'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'identity': {'key': 'identity', 'type': 'Identity'},
    }

    def __init__(self, location, tags=None, plan=None, properties=None, kind=None, managed_by=None, sku=None, identity=None):
        super(GenericResource, self).__init__(location=location, tags=tags)
        self.plan = plan
        self.properties = properties
        self.kind = kind
        self.managed_by = managed_by
        self.sku = sku
        self.identity = identity
