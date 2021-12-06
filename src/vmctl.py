import os
from vm import VM
from config import CONFIGS


def fetch_all_vms():
    """
    :return: all of vm instances
    """

    vms = []
    chlidren_dirs = os.listdir(CONFIGS['vm_dir'])
    for child in chlidren_dirs:
        if child.endswith(CONFIGS['postfix_vm']):
            vms.append(VM(child))
    return vms


# Test
print(fetch_all_vms())
