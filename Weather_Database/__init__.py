
import os
import sys

config_dir = os.path.join(os.environ['userprofile'],'Path','To','dir1')
sys.path.append(config_dir)

from dir1 import config