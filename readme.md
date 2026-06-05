# RSA vs Shor's Algorithm

## Objective

This project demonstrates RSA encryption and decryption using Python and explores how Shor's Algorithm could impact RSA security in the future.

## About RSA
RSA is a public-key cryptographic system that uses two keys:

* Public Key: Used to encrypt data.
* Private Key: Used to decrypt data.

The security of RSA relies on the difficulty of factoring very large integers.

## Project Demonstration
The Python program:

1. Generates an RSA public and private key pair.
2. Accepts a user message.
3. Encrypts the message using the public key.
4. Decrypts the ciphertext using the private key.
5. Displays the original, encrypted, and decrypted messages.

## Technologies Used

* Python
* RSA Python Library

## How RSA Works

Message
↓
Public Key
↓
Encryption
↓
Ciphertext
↓
Private Key
↓
Decryption
↓
Original Message

## Impact of Shor's Algorithm

Shor's Algorithm is a quantum algorithm capable of factoring large integers much more efficiently than known classical algorithms.

Since RSA security depends on the hardness of factoring, sufficiently powerful quantum computers running Shor's Algorithm could compromise RSA-based systems.
## Why Post-Quantum Cryptography?

The development of quantum computers has motivated research into post-quantum cryptography, which aims to create cryptographic systems that remain secure against both classical and quantum attacks.

## Learning Outcomes

* Understood RSA key generation, encryption, and decryption.
* Implemented a basic RSA demonstration in Python.
* Explored the relationship between RSA security and integer factorization.
* Learned how Shor's Algorithm motivates the transition toward post-quantum cryptography.
