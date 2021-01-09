# %%
import datetime

def datetime_format():return datetime.datetime.now().ctime()

def logger(name,value):return f"[{datetime_format()}] {name} ==> {value}"
# %%
