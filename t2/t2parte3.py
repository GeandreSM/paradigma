#!/usr/bin/env python3
from lxml import html, etree
import requests

## Desenvolvido em Python versão 3.5.2
def main():
   url = 'http://desafio-paradigmas.appspot.com'
   page = requests.get(url)
   tree = html.fromstring(page.content)
   content = tree.xpath("//p")
   string=page.text
   i=142 #Indice onde começa o código hexadecimal na string
   x=0
   while (x!=1):
      if str(string[i])+str(string[i+1])+str(string[i+2])!="-->": #verifica o fim do comentário para cortar a string só no código hex
         if i==142:
            aux=string[i]
            i=i+1
         else:
            aux=str(aux)+string[i]
            i=i+1
      else:
         x=1
   i=0
   while(i<len(aux)-1):#remove um \n que sobrou na string
      if i==0:
         temp=aux[i]
      else:
         temp=temp+aux[i]
      i=i+1
   string=temp
   string=[string[n] for n in range(0,len(string)) if string[n-1]!=' ' and string[n]!=' ' or string[n+1]!=' ']
   string=[string[n] for n in range(0,len(string)) if string[n]!=' '] #remove espaços
   string="".join(string)#converte a lista string para string
   return bytes.fromhex(string).decode('utf-8')##decodifica o código hexadecimal

if __name__ == '__main__':
   main()
