import rsa

# Open key file and return key data
def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


def verify(public_key_dir,file_dir,signature_dir):
    # Open public key file and load in key
    pubkey = rsa.PublicKey.load_pkcs1(file_open(public_key_dir+'/publickey.key'))

    # message = file_open('message')
    message = file_open(file_dir)
    signature = file_open(signature_dir+'/signature_file')

    # Verify the signature to show if successful or failed
    try:
        rsa.verify(message,signature,pubkey)
        print("Signature successfully verified")

    except:
        print("Warning!!!! Signature could not be verified\nFile has been tempered")
    
