# %%
import rsa
import os

def gen_keys(dir=''):
    """
    function take in file directory, generate the
    public and private key and store it in the given file directory
    """
    pub_dir = os.path.join(dir,"publickey.key")
    priv_dir = os.path.join(dir,'privatekey.key')


    log = f"""
        keys directory

        {pub_dir}
        {priv_dir}

        ===================================================
    """

    # create the pub & private keys
    (pubkey, privkey) = rsa.newkeys(2048)

    # write the public key to a file
    with open(pub_dir, 'wb') as key_file:
        key_file.write(pubkey.save_pkcs1('PEM'))
        
    

    # write the private key to a file
    with open(priv_dir, 'wb') as key_file:
        key_file.write(privkey.save_pkcs1('PEM'))

    print(log)

# %%
