# %%
import importlib
import pkgutil
import argparse


# Create the parser
parser = argparse.ArgumentParser(description='commands analysis conduct forensic on file')

# file path
parser.add_argument('--file','-f',
                    type=str,
                       help='path to where the file located')


args = parser.parse_args()







# %%
if __name__ == "__main__":

    # load plugins
    discovered_plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in pkgutil.iter_modules()
        if name.startswith('plug_')
    }


    # generate results for each of the plugins
    result = list()
    for plug in discovered_plugins:
        result +=discovered_plugins[plug].run(args.file)


    # print to the console
    for data in result:
        print(data)

# %%
