#1 Defina uma função somaQuad(x,y) que calcule a soma dos quadrados de dois números x e y.

def	somaQuad(x,y):
	return x*x+y*y
#2 Crie uma função hasEqHeads(l1,l2) que verifique se as listas l1 e l2 possuem o mesmo primeiro elemento.

def hasEqHeads(l1,l2):
	if l1[0]==l2[0]:
		return True
	else:
		return False
#3 Escreva uma função que receba uma lista de nomes e retorne uma lista com a string "Sr. " adicionada ao início de cada nome. Defina uma função auxiliar para ajudar neste exercício.


def addstringaux(str):
	return 'SR. '+str

def addstring(lista):
	return list(map(addstringaux,lista))

#4 Crie uma função que receba uma string e retorne o número de espaços nela contidos. Defina uma função auxiliar para ajudar neste exercício.

def strspace(str):
	return len(list(filter(lambda x:x==' ',str)))
#5 Escreva uma função que, dada uma lista de números, calcule 3n*2 + 2/n + 1 para cada número n da lista. Defina uma função auxiliar para ajudar neste exercício.

def calcaux(n):
	return 3*n*2+2/n+1
def calc(lis):
	return list(map(calcaux,lis))
#6 Escreva uma função que, dada uma lista de números, retorne uma lista com apenas os que forem negativos. Defina uma função auxiliar para ajudar neste exercício.

def negativo(lis):
	return list(filter(lambda n: n<0,lis))
#7 Escreva uma função que receba uma lista de números e retorne somente os que estiverem entre 1 e 100, inclusive. Defina uma função auxiliar para ajudar neste exercício.

def entre1e100(lis):
	return list(filter(lambda n: n>1 and n<100,lis))
#8 Escreva uma função que receba uma lista de números e retorne somente aqueles que forem pares. Defina uma função auxiliar para ajudar neste exercício.

def filtrapar(lis):
	return list(filter(lambda n:n%2==0,lis))
#9 Crie uma função charFound(c,s) que verifique se o caracter c está contido na string. O resultado deve ser True ou False. Você não deve usar o operador in. Defina uma função auxiliar para ajudar neste exercício.

def charFoud(c,s):
	if len(s)<1:
		return False
	elif s[0]==c:
		return True
	else:
		return charFoud(c,s[1:])

#10 Escreva uma função que receba uma lista de strings e retorne uma nova lista com adição de marcações HTML (p.ex.: <B> e </B>) antes e depois de cada string.

def addhtml(lista):
	return list(map(lambda x: "<B>"+x+"</B>",lista))