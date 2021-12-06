import sys
import os
import json

with open('config.json') as f:
    j_data = json.load(f)
    print(j_data['vm_dir'])