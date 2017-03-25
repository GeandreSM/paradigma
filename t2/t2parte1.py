#1 Defina uma função addSuffix(suf,nomes) que retorne a lista de nomes com o sufixo suf adicionado. Exemplos:
def addsufix(x,s):
   return [s+x for w in s]

#2 Escreva uma função countShorts(words), que receba uma lista de palavras e retorne a quantidade de palavras dessa lista que possuem menos de 5 caracteres.

def countshort(w):
   return len([w for w in w if len(w)<5])

#3 Defina uma função stripVowels(s) que receba uma string e retire suas vogais, conforme os exemplos abaixo:

def stripVowels(str):
    return[str for str in str if not str in 'aeiouAEIOU']

#4 Defina uma função hideChars(s) que receba uma string, possivelmente contendo espaços, e que retorne outra string substituindo os demais caracteres por '-', mas mantendo os espaços. Exemplos:

def hideChars(s):
    return"".join(['-' if not c==' ' else c for c in s])

#5 Defina uma função que receba um número n e retorne uma tabela de números de 1 a n e seus quadrados, conforme os exemplos abaixo (você vai usar tuplas em Python):

def gentable(x):
     return [(n,n*n) for n in range(1,x)]

#6 Defina uma função que receba uma lista de palavras e retorne uma string contendo o primeiro e o último caracter de cada palavra da lista. Exemplo:

def genCode(lis):
	return "".join([x[0]+x[-1] for x in lis])

#7 Defina uma função myZip(l1,l2) que reproduza o comportamento da função zip do Python:

def myZip(lis,ta):
	return [(lis[x],ta[x]) for x in range(len(lis))]

#8 Escreva uma função enumerate(words) que numere cada palavra da lista recebida:

def enumerate(words):
	return [(x+1,words[x]) for x in range(len(words))]

#9 Escreva uma função isBin(s) que verifique se a string recebida representa um número binário. Exemplo:

def isBin(s):
	return len([x for x in s if not x in'01']) <1

#10 Escreva uma função bin2dec(digits), que receba uma lista de dígitos representando um número binário e retorne seu equivalente em decimal. Exemplo:

def bin2dec(lista):
	return sum(([lista[(len(lista)-1)-x]*(2**x) for x in range(len(lista))]))