import random
import sys
import string
import argparse

parser = argparse.ArgumentParser(description='Generate password of a specific length')
parser.add_argument('-l','--passlen', metavar='L', type=int,
                    default=10,
                    help='Length of the pasword to be generated')
args = parser.parse_args()

def passgen(passlen):
    """
    function takes in the length of the password to br generated and returns the generated password
    parameter:
        passlen:int

    return:
        password:str
    """

    # combination of letters both uppercase and lowercase,punctuation,digit
    chars = string.ascii_letters+string.digits+'-&%$#@*'

    # randomly select chars based on the length given
    password = ''.join([random.choice(chars) for _ in range(passlen)])
    
    print(f"new password generated\n======> {password}\nlength {passlen}")
    sys.exit()
    return password



if __name__ == "__main__":
    passgen(int(args.passlen))
