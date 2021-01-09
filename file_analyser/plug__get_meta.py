# %%

from utilities import datetime_format,logger
import magic
import  filetype



def run(file_path,*args, **kwargs):
    result = list()


    # extract meta data and signature
    data = magic.from_buffer(open(file_path, "rb").read(2048)).split(',')
    
    result =[
        logger("signature",data[0])
        
    ]

    if len(data) > 1:
        for x in data[1:]:result.append(logger("meta",x))


    # get mime type
    mime = magic.from_file(file_path, mime=True)
    result.append(logger("mime-type",mime))

    try:
        # get extension
        kind = filetype.guess(file_path)
        result.append(logger("original extension",f".{kind.extension}"))
    except:
        pass
    
    ext = file_path.split('.')
    if ext:result.append(logger("current extension",f".{ext[-1]}"))
    

    return result
# %%

