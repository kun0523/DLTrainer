import os
import shutil
from datetime import datetime


def create_dir(target_dir):
    if os.path.isdir(target_dir):
        shutil.rmtree(target_dir)
    os.makedirs(target_dir)
    return os.path.abspath(target_dir)


def get_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")


def get_timenow():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def copy_files(src_dir, dst_dir, files):
    for file in files:
        tmp_pth = os.path.join(src_dir, file)
        if not os.path.isfile(tmp_pth): continue
        shutil.copyfile(tmp_pth, os.path.join(dst_dir, file))
    return
