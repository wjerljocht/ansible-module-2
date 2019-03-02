#!/usr/bin/env python3
import yaml
from ansible.module_utils.basic import AnsibleModule

fields = '''
    foo:
        required: yes
        type: str
    bar:
#       required: no
        type: dict
'''
fields = yaml.load(fields)

#/usr/local/lib/python3.6/dist-packages/ansible/module_utils/basic.py
ansible = AnsibleModule(argument_spec=fields)
#for key, value in ansible.params.items():
#    if value:
#        ansible.params[key] = value.upper()
msg=ansible.params
msg['fokke'] = 'sukke'
ansible.exit_json(msg=msg)
