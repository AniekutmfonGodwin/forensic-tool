import argparse
from create_keys import gen_keys
from hash_message import sign
from decrypt_all import verify
import os

# Import the argparse library
import argparse

import os
import sys

# Create the parser
parser = argparse.ArgumentParser(description='List the content ')



# generate keys
parser.add_argument('--workspace','-ws',
                       type=str,
                       default='workspace',
                       help='Path to where to sto the public and private keys')

parser.add_argument('--gen','-g',
                    #    type=bool,
                       action='store_true',
                       help='Path to where to sto the public and private keys')



# sign files
parser.add_argument('--sign','-s',
                       action='store_true',
                       help='Path to where to sto the public and private keys')





parser.add_argument('--file','-f',
                    type=str,
                       help='Path to where to sto the public and private keys')





# verify file
parser.add_argument('--verify','-v',
                    action='store_true',
                       help='Path to where to sto the public and private keys')






args = parser.parse_args()

if args.workspace == 'workspace' and not os.path.isdir('workspace'):
    print(args.workspace)
    os.mkdir('workspace')
    

# flag for generating public and private keys
if args.gen:
    gen_keys(args.workspace)

# flag for signing a file 
elif args.sign:
    sign(args.workspace,args.file,args.workspace)

# flag for verifying a flag
elif args.verify:
    verify(args.workspace,args.file,args.workspace)

