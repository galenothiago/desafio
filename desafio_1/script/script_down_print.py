#!/bin/python3
import os
from os import walk
import shutil 
import urllib

URL_DOWNLOAD = 'http://0.0.0.0:8085/desafio.tar'

desafio = '/home/thiago/Documentos/desafio_nginx/desafio'

urllib.request.urlretrieve(URL_DOWNLOAD, 'desafio.tar')

filename = "desafio.tar"
shutil.unpack_archive(filename)  

files = []

for (dirpath, dirnames, filenames) in walk(desafio):
  files.extend(filenames)
  break

stringABC = ''
os.chdir(desafio)

for file in files:
  if not file.startswith('.'):
    with open(file, 'r') as text:
      a = text.readlines()
      if ((a[1]) == 'b' or (a[1]) == 'a' or (a[1]) == 'c'):
        if a[1] not in stringABC:
          stringABC+=a[1]


print('As strings são: \n')
print(stringABC)

