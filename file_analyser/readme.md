# Use cases
## Analyse file

    ...> analyse -f [file path]




## Creating a Plugin
### plugin is a file that starts with `plug_*`
### plugin file must contain a function name run which takes in a file_path and return a list of a logger function output. The logger can be imported from utilities
    from utilities import logger
### the logger function takes the name of an attribute and the value of the attribute and return a log format
    def run(file_path,*args,**kwargs):
        return [logger(name,value)]






