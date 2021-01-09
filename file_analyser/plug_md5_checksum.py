# %%
import hashlib
from utilities import datetime_format,logger


def run(file_path,*args, **kwargs):
    hasher = hashlib.md5()
    with open(file_path,'rb') as open_file:
        content = open_file.read()
        hasher.update(content)

    return [logger("check-sum",hasher.hexdigest())]
# %%


# %%
