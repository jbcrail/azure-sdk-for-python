# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class ExpressRouteCircuit(Resource):
    """
    ExpressRouteCircuit resource

    :param str id: Resource Id
    :param str name: Resource name
    :param str type: Resource type
    :param str location: Resource location
    :param dict tags: Resource tags
    :param ExpressRouteCircuitSku sku: Gets or sets sku
    :param str etag: Gets a unique read-only string that changes whenever the
     resource is updated
    :param str circuit_provisioning_state: Gets or sets
     CircuitProvisioningState state of the resource
    :param str service_provider_provisioning_state: Gets or sets
     ServiceProviderProvisioningState state of the resource . Possible values
     include: 'NotProvisioned', 'Provisioning', 'Provisioned',
     'Deprovisioning'
    :param list authorizations: Gets or sets list of authorizations
    :param list peerings: Gets or sets list of peerings
    :param str service_key: Gets or sets ServiceKey
    :param str service_provider_notes: Gets or sets ServiceProviderNotes
    :param ExpressRouteCircuitServiceProviderProperties
     service_provider_properties: Gets or sets ServiceProviderProperties
    :param str provisioning_state: Gets or sets Provisioning state of the
     PublicIP resource Updating/Deleting/Failed
    """

    _required = []

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'ExpressRouteCircuitSku'},
        'etag': {'key': 'etag', 'type': 'str'},
        'circuit_provisioning_state': {'key': 'properties.circuitProvisioningState', 'type': 'str', 'flatten': True},
        'service_provider_provisioning_state': {'key': 'properties.serviceProviderProvisioningState', 'type': 'ServiceProviderProvisioningState', 'flatten': True},
        'authorizations': {'key': 'properties.authorizations', 'type': '[ExpressRouteCircuitAuthorization]', 'flatten': True},
        'peerings': {'key': 'properties.peerings', 'type': '[ExpressRouteCircuitPeering]', 'flatten': True},
        'service_key': {'key': 'properties.serviceKey', 'type': 'str', 'flatten': True},
        'service_provider_notes': {'key': 'properties.serviceProviderNotes', 'type': 'str', 'flatten': True},
        'service_provider_properties': {'key': 'properties.serviceProviderProperties', 'type': 'ExpressRouteCircuitServiceProviderProperties', 'flatten': True},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str', 'flatten': True},
    }

    def __init__(self, id=None, name=None, type=None, location=None, tags=None, sku=None, etag=None, circuit_provisioning_state=None, service_provider_provisioning_state=None, authorizations=None, peerings=None, service_key=None, service_provider_notes=None, service_provider_properties=None, provisioning_state=None):
        super(ExpressRouteCircuit, self).__init__(id=id, name=name, type=type, location=location, tags=tags)
        self.sku = sku
        self.etag = etag
        self.circuit_provisioning_state = circuit_provisioning_state
        self.service_provider_provisioning_state = service_provider_provisioning_state
        self.authorizations = authorizations
        self.peerings = peerings
        self.service_key = service_key
        self.service_provider_notes = service_provider_notes
        self.service_provider_properties = service_provider_properties
        self.provisioning_state = provisioning_state
