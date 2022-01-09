#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by vmware_rest_code_generator.
# See: https://github.com/ansible-collections/vmware_rest_code_generator
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: content_locallibrary_info
short_description: Returns a given local library.
description: Returns a given local library.
options:
  library_id:
    description:
    - Identifier of the local library to return. Required with I(state=['get'])
    type: str
  session_timeout:
    description:
    - 'Timeout settings for client session. '
    - 'The maximal number of seconds for the whole operation including connection
      establishment, request sending and response. '
    - The default value is 300s.
    type: float
    version_added: 2.1.0
  vcenter_hostname:
    description:
    - The hostname or IP address of the vSphere vCenter
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_HOST) will be used instead.
    required: true
    type: str
  vcenter_password:
    description:
    - The vSphere vCenter password
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_PASSWORD) will be used instead.
    required: true
    type: str
  vcenter_rest_log_file:
    description:
    - 'You can use this optional parameter to set the location of a log file. '
    - 'This file will be used to record the HTTP REST interaction. '
    - 'The file will be stored on the host that run the module. '
    - 'If the value is not specified in the task, the value of '
    - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
    type: str
  vcenter_username:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_USER) will be used instead.
    required: true
    type: str
  vcenter_validate_certs:
    default: true
    description:
    - Allows connection when SSL certificates are not valid. Set to C(false) when
      certificates are not trusted.
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_VALIDATE_CERTS) will be used instead.
    type: bool
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 2.0.0
requirements:
- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.2
"""

EXAMPLES = r"""
- name: Build a list of local libraries
  vmware.vmware_rest.content_locallibrary_info:
  register: result
  retries: 100
  delay: 3
  until: result is not failed

- name: Create a new local content library
  vmware.vmware_rest.content_locallibrary:
    name: local_library_001
    description: automated
    publish_info:
      published: true
      authentication_method: NONE
    storage_backings:
    - datastore_id: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/rw_datastore')\
        \ }}"
      type: DATASTORE
    state: present
  register: ds_lib

- name: Retrieve the local content library information based upon id check mode
  vmware.vmware_rest.content_locallibrary_info:
    library_id: '{{ ds_lib.id }}'
  register: result
  check_mode: true
"""

RETURN = r"""
# content generated by the update_return_section callback# task: Retrieve the local content library information based upon id check mode
id:
  description: moid of the resource
  returned: On success
  sample: 712b11c1-972a-4c22-99d5-e3046a92c9ec
  type: str
value:
  description: Retrieve the local content library information based upon id check
    mode
  returned: On success
  sample:
    creation_time: '2022-01-04T21:29:00.266Z'
    description: automated
    id: 712b11c1-972a-4c22-99d5-e3046a92c9ec
    last_modified_time: '2022-01-04T21:29:00.266Z'
    name: local_library_001
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/712b11c1-972a-4c22-99d5-e3046a92c9ec/lib.json
      published: 1
      user_name: vcsp
    server_guid: c6a81a4c-3386-4a6a-a909-a52bd5c9bafa
    storage_backings:
    - datastore_id: datastore-1087
      type: DATASTORE
    type: LOCAL
    version: '2'
  type: dict
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "get": {"query": {}, "body": {}, "path": {"library_id": "library_id"}},
    "list": {"query": {}, "body": {}, "path": {}},
}  # pylint: disable=line-too-long

import json
import socket
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
    session_timeout,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["library_id"] = {"type": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: info_list_and_get_module.j2
def build_url(params):
    if params.get("library_id"):
        _in_query_parameters = PAYLOAD_FORMAT["get"]["query"].keys()
        return (
            ("https://{vcenter_hostname}" "/api/content/local-library/").format(
                **params
            )
            + params["library_id"]
            + gen_args(params, _in_query_parameters)
        )
    _in_query_parameters = PAYLOAD_FORMAT["list"]["query"].keys()
    return ("https://{vcenter_hostname}" "/api/content/local-library").format(
        **params
    ) + gen_args(params, _in_query_parameters)


async def entry_point(module, session):
    url = build_url(module.params)
    async with session.get(url, **session_timeout(module.params)) as resp:
        _json = await resp.json()

        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}

        if module.params.get("library_id"):
            _json["id"] = module.params.get("library_id")
        elif module.params.get("label"):  # TODO extend the list of filter
            _json = await exists(module.params, session, url)
        elif (
            isinstance(_json["value"], list)
            and len(_json["value"]) > 0
            and isinstance(_json["value"][0], str)
        ):
            # this is a list of id, we fetch the details
            full_device_list = await build_full_device_list(session, url, _json)
            _json = {"value": [i["value"] for i in full_device_list]}

        return await update_changed_flag(_json, resp.status, "get")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.get_event_loop_policy().get_event_loop()
    current_loop.run_until_complete(main())
