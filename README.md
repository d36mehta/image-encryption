# Encrypting images using AES (CBC mode)

- Uses a random (pseudorandom from os.urandom) initial vector and adds padding to encrypt and decrypt images

- unfortunate problems: https://docs.microsoft.com/en-us/dotnet/standard/security/vulnerabilities-cbc-mode

![funny](https://user-images.githubusercontent.com/52871085/190058311-d296bc05-8b0f-49aa-b678-0feec6a14274.png)
