
# %%
import filecmp
from utilities import logger
from datetime import datetime
import os
import stat

def run(file_path,*args, **kwargs):
    result = list()

    # rep file size
    size = os.stat(file_path).st_size
    result.append(logger("size",f"{size/1000}kb"))

    # last access time in seconds
    last_accessed = datetime.fromtimestamp(os.stat(file_path).st_atime).ctime()
    result.append(logger("last accessed",last_accessed))

    # last modify in seconds
    last_modified = datetime.fromtimestamp(os.stat(file_path).st_mtime).ctime()
    result.append(logger("last modify",last_modified))

    # last changed in seconds
    last_changed = datetime.fromtimestamp(os.stat(file_path).st_ctime).ctime()
    result.append(logger("last changed",last_changed))

    return result


