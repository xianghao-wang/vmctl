import os

CONFIGS = {
    # the directory of all virtual machines
    'vm_dir': os.environ.get('HOME') + '/Virtual Machines.localized/',

    # the post fix of the directory of each virtual machine
    'postfix_vm': '.vmwarevm',

    # the option of starting virtual machine
    'op': 'nogui'
}