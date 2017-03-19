
#1 Escreva uma função que receba uma lista de nomes e retorne uma lista com a string "Sr. " adicionada ao início de cada nome.

def addstring(lista):
	return list(map(lambda x:"SR. "+x,lista))
#2 Escreva uma função que, dada uma lista de números, calcule 3n*2 + 2/n + 1 para cada número n da lista.

def calc(lis):
	return list(map(lambda n: 3*n*2+2/n+1,lis))
#3 Crie uma função que receba uma lista de nomes e retorne outra lista com somente aqueles nomes que terminarem com a letra 'a'.

def terminacomA(lista):
	return list(filter(lambda x: x[-1]=='a',lista))
#4 Escreva uma função que, dada uma lista de idades de pessoas no ano atual, retorne uma lista somente com as idades de quem nasceu depois de 1970. Para testar a condição, sua função deverá subtrair a idade do ano atual.

def idades(lista):
	return list(filter(lambda n: 2017-n>1970,lista))
#5 O código abaixo é escrito em Python imperativo. Escreva um código equivalente usando programação funcional.
def func(lista):
	return list(map(lambda n: n*2,lista))
