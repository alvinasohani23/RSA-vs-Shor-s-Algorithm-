import rsa
print("=== RSA Encryption Demo ===")
# Generate RSA keys
public_key, private_key = rsa.newkeys(512)
# User enters a message
message = input("Enter a message: ")
# Encrypt the message
encrypted_message = rsa.encrypt(message.encode(), public_key)
# Decrypt the message
decrypted_message = rsa.decrypt(encrypted_message, private_key)
print("\nOriginal Message:")
print(message)
print("\nEncrypted Message:")
print(encrypted_message)
print("\nDecrypted Message:")
print(decrypted_message.decode())
print("\nRSA demonstration completed successfully!")
