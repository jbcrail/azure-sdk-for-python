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


class JobSchedulePatchParameter(Model):
    """Parameters for a CloudJobScheduleOperations.Patch request.

    :param schedule: The schedule according to which jobs will be created. If
     you do not specify this element, the existing schedule is not modified.
    :type schedule: :class:`Schedule <azure.batch.models.Schedule>`
    :param job_specification: The details of the jobs to be created on this
     schedule.
    :type job_specification: :class:`JobSpecification
     <azure.batch.models.JobSpecification>`
    :param metadata: A list of name-value pairs associated with the job
     schedule as metadata.
    :type metadata: list of :class:`MetadataItem
     <azure.batch.models.MetadataItem>`
    """ 

    _attribute_map = {
        'schedule': {'key': 'schedule', 'type': 'Schedule'},
        'job_specification': {'key': 'jobSpecification', 'type': 'JobSpecification'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
    }

    def __init__(self, schedule=None, job_specification=None, metadata=None):
        self.schedule = schedule
        self.job_specification = job_specification
        self.metadata = metadata
