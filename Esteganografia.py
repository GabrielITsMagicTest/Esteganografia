#!/usr/bin/python3
# /tmp/steganohelp.py
# Um exemplo de uso de Steganographuy

import os, inspect;

from PIL import Image
from Crypto.Random import get_random_bytes;

from ciphers.aes import AesHelper;
from ciphers.blowfish import BlowfishHelper
from ciphers.chacha20 import ChaChaHelper
from ciphers.salsa20 import SalsaHelper



#       MEXAR NESSA VARIAVEIS

#! onde esta a imagem
path_imagem = "/hacker.png"

#! cipher = algoritimo criptografia
#! cipher = (AesHelper, BlowfishHelper, ChaChaHelper, SalsaHelper)
cipher = ChaChaHelper
#! chave do cipher = algoritimo criptografia
key = "123456"

#       FIM DAS VARIAVEIS




class SteganoHelper():
	def __init__(self, crypt=None):
		self.crypt = crypt;

	# pegar os simbolos em binario
	def genData(self, data):
		newd = [];
		for i in data:
			newd.append(format(ord(i), '08b'))
		return newd;

	# modificar os 9 RGB para para poder ler
	def modPix(self, pix, data):
		datalist = self.genData(data); # binario do simbolo
		lendata = len(datalist); # quantos simbolos tem
		imdata = iter(pix); # pegar os rgb de cada pixel da imagem.

		for i in range(lendata):
			# 9 numeros, 3 rgb [(r,g,b) (r,g,b) (r,g,b)]
			pix = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]];
			# escrever para cada
			for j in range(0, 8):
				# se for impar virar par, se for par virar impar. 0 e par, 1 e impar
				# se e 0 e impar.
				if (datalist[i][j] == '0' and pix[j] % 2 != 0):
					# transforma em par
					pix[j] -= 1; 

				# se e 1 e par.
				elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
					# trasnforma em impar
					if (pix[j] != 0):
						pix[j] -= 1;
					else: # pra não dar -1 e sim 1. -1 nao e um numero pra usar no rgb
						pix[j] += 1;

			# impar no ultimo digito significa que ja terminou(vai ser util na leitura), par continue lendo
			if (i == lendata - 1):
				if (pix[-1] % 2 == 0):
					if (pix[-1] != 0):
						pix[-1] -=1;
					else: # pra não dar -1 e sim 1. -1 nao e um numero pra usar no rgb
						pix[-1] += 1;
			else: # continue lendo
				if (pix[-1] % 2 != 0): # se e impar mudar para par
					pix[-1] -= 1;

			pix = tuple(pix)
			yield pix[0:3];
			yield pix[3:6];
			yield pix[6:9];

	# adicionar as modificação na imagem
	def encode_enc(self, newimg, data):
		w = newimg.size[0];
		(x, y) = (0, 0)

		for pixel in self.modPix(newimg.getdata(), data):
			newimg.putpixel((x,y), pixel);
			if (x == w - 1):
				x = 0;
				y += 1;
			else:
				x +=1;

	# criar a imagem com steganografia
	def encode(self, path_img, message, prefix="stegano"):
		if not os.path.exists(path_img):
			return False;
		if self.crypt != None:
			message = self.crypt.encrypt(message);

		image = Image.open(path_img, "r");
		newimg = image.copy();

		self.encode_enc(newimg, message);

		new_image_name = path_img[:path_img.rfind(".")] + "_" + prefix + "_" + path_img[path_img.rfind("."):];
		if os.path.exists(new_image_name):
			os.unlink(new_image_name);

		newimg.save(new_image_name, str(new_image_name.split(".")[1].upper()));
		return True;

	# ler a imagem com steganografia
	def decode(self, path_img):
		if not os.path.exists(path_img):
			return None;

		image = Image.open(path_img, 'r');
		data = "";
		imgdata = iter(image.getdata());

		while True:
			pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3] ];
			binstr = "";
			for i in pixels[:8]:
				if (i % 2 == 0):     # se e par
					binstr += "0";
				else:                # se e impar
					binstr += "1";

			# ler binario
			data += chr(int(binstr, 2));
			if (pixels[-1] % 2 != 0):
				if self.crypt != None:
					data = self.crypt.decrypt(data);
				return data;

# so pra rodar localmente pra ver como funciona
if __name__ == '__main__':
	key = key.ljust(32, "s").encode(); # preenchendo a chave com 's'
	cipher = cipher(key)

	# Diretorio do script
	DIRNAME = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

	stg = SteganoHelper(crypt=cipher);
	stg.encode(DIRNAME+path_imagem, "<texto que sera criptografado> suporta muitas linhas hahahahahhahahahhaaahhaahahahhahah mas tem quer ser grande o arquivo haha");
	print("foi obtido da imagem: ", stg.decode(DIRNAME+ path_imagem[:path_imagem.rfind(".")] +"_stegano_.png"));