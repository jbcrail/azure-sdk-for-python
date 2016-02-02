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

from .sub_resource import SubResource


class SecurityRule(SubResource):
    """
    Network security rule

    :param str id: Resource Id
    :param str name: Gets name of the resource that is unique within a
     resource group. This name can be used to access the resource
    :param str etag: A unique read-only string that changes whenever the
     resource is updated
    :param str description: Gets or sets a description for this rule.
     Restricted to 140 chars.
    :param str protocol: Gets or sets Network protocol this rule applies to.
     Can be Tcp, Udp or All(*). Possible values include: 'Tcp', 'Udp', '*'
    :param str source_port_range: Gets or sets Source Port or Range. Integer
     or range between 0 and 65535. Asterix '*' can also be used to match all
     ports.
    :param str destination_port_range: Gets or sets Destination Port or
     Range. Integer or range between 0 and 65535. Asterix '*' can also be
     used to match all ports.
    :param str source_address_prefix: Gets or sets source address prefix.
     CIDR or source IP range. Asterix '*' can also be used to match all
     source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer'
     and 'Internet' can also be used. If this is an ingress rule, specifies
     where network traffic originates from.
    :param str destination_address_prefix: Gets or sets destination address
     prefix. CIDR or source IP range. Asterix '*' can also be used to match
     all source IPs. Default tags such as 'VirtualNetwork',
     'AzureLoadBalancer' and 'Internet' can also be used.
    :param str access: Gets or sets network traffic is allowed or denied.
     Possible values are 'Allow' and 'Deny'. Possible values include:
     'Allow', 'Deny'
    :param int priority: Gets or sets the priority of the rule. The value can
     be between 100 and 4096. The priority number must be unique for each
     rule in the collection. The lower the priority number, the higher the
     priority of the rule.
    :param str direction: Gets or sets the direction of the rule.InBound or
     Outbound. The direction specifies if rule will be evaluated on incoming
     or outcoming traffic. Possible values include: 'Inbound', 'Outbound'
    :param str provisioning_state: Gets or sets Provisioning state of the
     PublicIP resource Updating/Deleting/Failed
    """

    _required = ['protocol', 'source_address_prefix', 'destination_address_prefix', 'access', 'direction']

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str', 'flatten': True},
        'protocol': {'key': 'properties.protocol', 'type': 'SecurityRuleProtocol', 'flatten': True},
        'source_port_range': {'key': 'properties.sourcePortRange', 'type': 'str', 'flatten': True},
        'destination_port_range': {'key': 'properties.destinationPortRange', 'type': 'str', 'flatten': True},
        'source_address_prefix': {'key': 'properties.sourceAddressPrefix', 'type': 'str', 'flatten': True},
        'destination_address_prefix': {'key': 'properties.destinationAddressPrefix', 'type': 'str', 'flatten': True},
        'access': {'key': 'properties.access', 'type': 'SecurityRuleAccess', 'flatten': True},
        'priority': {'key': 'properties.priority', 'type': 'int', 'flatten': True},
        'direction': {'key': 'properties.direction', 'type': 'SecurityRuleDirection', 'flatten': True},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str', 'flatten': True},
    }

    def __init__(self, protocol, source_address_prefix, destination_address_prefix, access, direction, id=None, name=None, etag=None, description=None, source_port_range=None, destination_port_range=None, priority=None, provisioning_state=None):
        super(SecurityRule, self).__init__(id=id)
        self.name = name
        self.etag = etag
        self.description = description
        self.protocol = protocol
        self.source_port_range = source_port_range
        self.destination_port_range = destination_port_range
        self.source_address_prefix = source_address_prefix
        self.destination_address_prefix = destination_address_prefix
        self.access = access
        self.priority = priority
        self.direction = direction
        self.provisioning_state = provisioning_state
