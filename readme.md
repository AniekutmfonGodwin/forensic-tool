# Documentation
### This CLI tool is build with python ,to use it first 
### Install dependencies with
    pip install -r requirements.txt

### also download install [VCForPython](https://www.microsoft.com/en-us/download/details.aspx?id=44266) and you can now run your commands



&nbsp;
## Hash and sign a file
### to generate a public and private keys
    ...> hash -g -ws [output dir:optional]
### a pubic and a private key will be generated and store in the given folder specified 


&nbsp; 

### To sign a file run
    ...> hash -s -f [file path] -ws [output dir :optional]
#### the specified file will be sign with the owners private key which will be located in the output directory given  and generate a signature file which will be stored in the output folder specified

&nbsp; 



### verify a file using the public key and the signature, enter the file path and the workspace folder where the public key file is stored
    ...> hash -v -f [file path] -ws [output dir :optional]


&nbsp;


## Password Generator
### Password generator Commands 
    ...>pgen -l [length of password]
### the length is the length of password to be generated.
### the generated password is printed on the console

&nbsp;


## Analyze  a file
### to analyse a file to extract its infoemation run. where file path is the path to the file to be used

    ...> analyse -f [file path]

&nbsp;

### Creating a Plugin
#### plugin is a file that starts with `plug_*` and exist in the `/file_analyser` directory
#### plugin file must contain a function name run which takes in a file_path and return a list of a logger function output. The logger can be imported from utilities
    from utilities import logger
#### the logger function takes the name of an attribute and the value of the attribute and return a log format
    def run(file_path,*args,**kwargs):
        return [logger(name,value)]

