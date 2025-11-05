#!/usr/bin/python3
# script: aes.py
# criptografar aes

import os, base64, random;

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes;

class AesHelper():
	def __init__(self, key=None, iv=None):
		if key == None:
			self.key = os.urandom(32);
		else:
			self.key = key;
		if iv == None:
			self.iv = os.urandom(16);
		else:
			self.iv = iv;

		self.cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv));

	def encrypt(self, message):
		message = base64.b64encode(message.encode()).decode();
		for i in range( 16 - (len(message) % 16 )):
			message += " ";
		encrypt = self.cipher.encryptor();
		result = self.iv + encrypt.update(message.encode("utf-8")) + encrypt.finalize();
		return base64.b64encode(result).decode("utf-8")

	def decrypt(self, message):
		message = base64.b64decode( message.encode("utf-8") )
		decryptor = self.cipher.decryptor();
		msg_nonce = message[:16];
		ciphertext = message[16:];
		result = decryptor.update(ciphertext) + decryptor.finalize()
		return base64.b64decode( (result).decode("utf-8")).decode("utf-8"); 

# if __name__ == "__main__":
# 	ae = AesHelper();
# 	criptografado = ae.encrypt("Este texto será criptografado")
# 	print(criptografado)
# 	print(ae.decrypt(criptografado))