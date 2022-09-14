import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

# encrypting images with AES encryption algorithm (CBC mode)
KEYSIZE = 16
BLKSIZE = 16

# input filename option
# filenameinput = input()
# filepathsplit = filenameinput.rsplit("/", 1)
# filepath = filepathsplit[0] + "/"
# filename = filepathsplit[1]
# newfilename = filepath + "encrypted_" + filename
# oldfilename = filepath + "decrypted_" + filename

# my grandma's favourite picture on my phone
filename = "funny.png"
# encrypted_so_not_funny.png
newfilename = "encrypted_so_not_" + filename
# decrypted_so_funny.png
oldfilename = "decrypted_so_" + filename


# generate keys and initialization vector randomly (pseudorandom)
def generateKeyOrInitVector(size):
    return os.urandom(size)


# use the key and vector to encrypt and decrypt using AES
def encryptImage(filename, key, initVector):
    with open(filename, "rb") as file:
        bytedata = file.read()
        # use AES algorithm in CBC mode and pad to fit full block
        aescipher = AES.new(key, AES.MODE_CBC, initVector)
        ct = aescipher.encrypt(pad(bytedata, BLKSIZE))
        # fill new file with cipher text
        with open(newfilename, "wb") as newfile:
            newfile.write(ct)


# now reverse for decryption
def decryptImage(filename, key, initVector):
    with open(filename, "rb") as file:
        bytedata = file.read()
        # get AES in CBC mode and unpad back to original size
        aescipher = AES.new(key, AES.MODE_CBC, initVector)
        ct = aescipher.decrypt(bytedata)
        ctunpad = unpad(ct, BLKSIZE)
        # fill new file with decrypted data (should be original image)
        with open(oldfilename, "wb") as oldfile:
            oldfile.write(ctunpad)


# set up key and vector, and call the encryption and decryption functions
key = generateKeyOrInitVector(KEYSIZE)

initVector = generateKeyOrInitVector(BLKSIZE)
# encryptImage(filenameinput, key, initVector)
encryptImage(filename, key, initVector)
decryptImage(newfilename, key, initVector)
