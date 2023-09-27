#!/usr/bin/python

#  Copyright: (c) 2023, DevInsight.
#  GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: my_test

short_description: This is my test module
"""

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        name=dict(type="str", required=True),
        new=dict(type="bool", required=False, default=False),
    )

    result = dict(changed=False, original_message="", message="")

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if module.check_mode:
        return result

    result["original_message"] = module.params["name"]
    result["message"] = "Goodbye"

    if module.params["name"] == "fail me":
        module.fail_json(msg="You requested this to fail", **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
