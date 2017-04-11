%Defina um predicado somaQuad(X,Y,Q) que seja verdadeiro se Q for a soma dos quadrados de X e Y. Exemplos de uso:

somaQuad(X,Y,Q) :-
	A is X^2,
	B is Y^2,
	Q is A+B.

%Defina um predicado zeroInit(L) que é verdadeiro se L for uma lista que inicia com o número 0 (zero). Exemplo de uso:
zeroInit(L) :-
	L=[H|_],
	H=:=0.

%Defina um predicado hasEqHeads(L1,L2) que seja verdadeiro se as listas L1 e L2 possuírem o mesmo primeiro elemento. Exemplos de uso:
hasEqHeads(L1,L2) :-
	L1=[H1|_],
	L2=[H2|_],
	H1=H2.

%Defina um predicado has5(L) que seja verdadeiro se L for uma lista de 5 elementos. Lembre de como funciona a unificação em Prolog e resolva este exercício sem usar o predicado pré-definido length. Exemplos de uso:
incrementa([],0).
incrementa(L,X) :-
	L=[_|T],
	incrementa(T,X1),
	X is 1+X1.
has5(L):-
	incrementa(L,X),
	X=:=5.

%Defina um predicado hasN(L,N) que seja verdadeiro se L for uma lista de N elementos. Agora você pode usar um predicado pré-definido.
hasN(L,N):-
	length(L,N).

%Defina um predicado isBin(L) que seja verdadeiro se L for uma lista contendo somente elementos 0 e 1. Use recursão. Exemplo:
isBin([0]).
isBin([1]).
isBin(L):-
	L=[H|T],
	H>(-1),
	H<2,
	isBin(T).

%Defina um predicado mesmaPosicao(A,L1,L2) para verificar se um elemento A está na mesma posição nas listas L1 e L2. Assuma que L1 e L2 sejam permutações de uma lista de elementos distintos, sem repetições. Dica: procure auxílio em predicados pré-definidos. Exemplo de uso:
mesmaPosicao(A,L1,L2):-
	nth0(X,L1,A),
        nth0(Y,L2,A),
	X=:=Y.

%Defina um predicado repete5(E,L) que seja verdadeiro se a lista L for composta por exatamente 5 repetições do elemento E. Não use recursão. Exemplos:
repete5(E,L) :-
	nth0(0,L,E),
	nth0(1,L,E),
	nth0(2,L,E),
	nth0(3,L,E),
	nth0(4,L,E).

%Defina um predicado recursivo sumQuads(L,S) que seja verdadeiro se S for o somatório dos quadrados dos elementos da lista L.
sumQuads([],0).
sumQuads(L,S):-
	L=[H|T],
	sumQuads(T,S1),
	S is  (H^2)+S1.


%Defina um predicado positivos(L1,L2), de forma que L2 seja uma lista só com os elementos positivos de L1, conforme o exemplo abaixo:
positivos([],[]).
positivos(L1,L2):-
	L1 = [H|T],
        H>0,
	L2 =[H|X],
	positivos(T,X).

positivos(L1,L2):-
	L1 = [H|T],
        H=<0,
        positivos(T,L2).








