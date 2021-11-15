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
module: vcenter_vm_guest_filesystem
short_description: Initiates an operation to transfer a file to or from the guest
description: 'Initiates an operation to transfer a file to or from the guest. <p>
  If the power state of the Virtual Machine is changed when the file transfer is in
  progress, or the Virtual Machine is migrated, then the transfer operation is aborted.
  <p> When transferring a file into the guest and overwriting an existing file, the
  old file attributes are not preserved. <p> In order to ensure a secure connection
  to the host when transferring a file using HTTPS, the X.509 certificate for the
  host must be used to authenticate the remote end of the connection. The certificate
  of the host that the virtual machine is running on can be retrieved using the following
  fields: XXX insert link to certificate in Host config XXX <p>'
options:
  attributes:
    description:
    - Details about the file to be transferred into the guest.
    - 'Valid attributes are:'
    - ' - C(size) (int): The size in bytes of the file to be transferred into the
      guest. ([''present''])'
    - '   This key is required with [''present''].'
    - ' - C(overwrite) (bool): Whether an existing file should be overwritten. ([''present''])'
    - ' - C(last_modified) (str): The date and time the file was last modified. ([''present''])'
    - ' - C(last_accessed) (str): The date and time the file was last accessed. ([''present''])'
    - ' - C(windows) (dict): Windows-specific file creation information. ([''present''])'
    - '   - Accepted keys:'
    - '     - hidden (boolean): The file is hidden.'
    - '     - read_only (boolean): The file is read-only.'
    - ' - C(posix) (dict): Posix-specific file creation information. ([''present''])'
    - '   - Accepted keys:'
    - '     - owner_id (integer): The owner ID. If this property is not specified
      when passing a {@link PosixFileAttributesCreateSpec} object to {@link Transfers#create},
      the default value will be the owner Id of the user who invoked the file transfer
      operation.'
    - '     - group_id (integer): The group ID. If this property is not specified
      when passing a {@link PosixFileAttributesCreateSpec} object to {@link Transfers#create},
      the default value will be the group Id of the user who invoked the file transfer
      operation.'
    - '     - permissions (string): The file permissions in chmod(2) format. If this
      property is not specified when passing a {@link PosixFileAttributesCreateSpec}
      object to {@link Transfers#create}, the file will be created with 0644 permissions.
      This field is interpreted as octal.'
    type: dict
  path:
    description:
    - The complete destination path in the guest to transfer the file to or from the
      client.  It cannot be a path to a directory or a symbolic link. This parameter
      is mandatory.
    required: true
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
  vm:
    description:
    - Virtual Machine to perform the operation on. This parameter is mandatory.
    required: true
    type: str
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
"""

RETURN = r"""
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "create": {
        "query": {},
        "body": {"attributes": "spec/attributes", "path": "spec/path"},
        "path": {"vm": "vm"},
    }
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

    argument_spec["attributes"] = {"type": "dict"}
    argument_spec["path"] = {"required": True, "type": "str"}
    argument_spec["vm"] = {"required": True, "type": "str"}

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


# template: default_module.j2
def build_url(params):
    return (
        "https://{vcenter_hostname}"
        "/api/vcenter/vm/{vm}/guest/filesystem?action=create"
    ).format(**params)


async def entry_point(module, session):

    func = globals()["_create"]

    return await func(module.params, session)


async def _create(params, session):

    payload = prepare_payload(params, PAYLOAD_FORMAT["create"])
    _url = (
        "https://{vcenter_hostname}"
        "/api/vcenter/vm/{vm}/guest/filesystem?action=create"
    ).format(**params)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        if resp.status == 500:
            text = await resp.text()
            raise EmbeddedModuleFailure(
                f"Request has failed: status={resp.status}, {text}"
            )
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}

        if (resp.status in [200, 201]) and "error" not in _json:
            if isinstance(_json, str):  # 7.0.2 and greater
                _id = _json  # TODO: fetch the object
            elif isinstance(_json, dict) and "value" not in _json:
                _id = list(_json["value"].values())[0]
            elif isinstance(_json, dict) and "value" in _json:
                _id = _json["value"]
            _json_device_info = await get_device_info(session, _url, _id)
            if _json_device_info:
                _json = _json_device_info

        return await update_changed_flag(_json, resp.status, "create")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
