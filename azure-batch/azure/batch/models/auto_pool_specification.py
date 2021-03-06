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

from msrest.serialization import Model


class AutoPoolSpecification(Model):
    """Specifies characteristics for a temporary 'auto pool'. The Batch service
    will create this auto pool, run all the tasks for the job on it, and will
    delete the pool once the job has completed.

    :param auto_pool_id_prefix: A prefix to be added to the unique identifier
     when a pool is automatically created. The prefix can be up to 20
     characters long.
    :type auto_pool_id_prefix: str
    :param pool_lifetime_option: The minimum lifetime of created auto pools,
     and how multiple jobs on a schedule are assigned to pools. Possible
     values include: 'jobschedule', 'job', 'unmapped'
    :type pool_lifetime_option: str or :class:`PoolLifetimeOption
     <azure.batch.models.PoolLifetimeOption>`
    :param keep_alive: Whether to keep an auto pool alive after its lifetime
     expires.
    :type keep_alive: bool
    :param pool: The pool specification for the auto pool.
    :type pool: :class:`PoolSpecification
     <azure.batch.models.PoolSpecification>`
    """ 

    _validation = {
        'pool_lifetime_option': {'required': True},
    }

    _attribute_map = {
        'auto_pool_id_prefix': {'key': 'autoPoolIdPrefix', 'type': 'str'},
        'pool_lifetime_option': {'key': 'poolLifetimeOption', 'type': 'PoolLifetimeOption'},
        'keep_alive': {'key': 'keepAlive', 'type': 'bool'},
        'pool': {'key': 'pool', 'type': 'PoolSpecification'},
    }

    def __init__(self, pool_lifetime_option, auto_pool_id_prefix=None, keep_alive=None, pool=None):
        self.auto_pool_id_prefix = auto_pool_id_prefix
        self.pool_lifetime_option = pool_lifetime_option
        self.keep_alive = keep_alive
        self.pool = pool
