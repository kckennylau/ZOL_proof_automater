This is an automater for proofs in zeroth-order logic (propositional logic).

It can prove every tautology, and it will error when given a statement that is not a tautology.

It operates under classical logic, and proceeds via what is essentially the semantic-completeness theorem.

First, it proves an instance of LEM for every variable that it encounters.

Then, it uses disjunction elimination and separates into as many cases as two to the power of the number of variables, and proves the theorem in each case by building up from the inside to the outside.

This is also my first attempt at writing a parser.

[Try it online!](https://tio.run/##7Vhtj9pGEP5s/4qNJSr7eNGRfkNHJZCuUqWkSqT2E6GVgT1YYWzLu6S5Rslfv87smxdjsKHX9FT1E/syz@zMMzO7ZvJHscnS75@ePsYFixcJ5WRMOBVh5Ptv7t/CJAiCnx5ImgkSks@3X0hWyAkOo5HvwR4MYeAdbg5gpR6EOz/GCacwKIWP0FoEF07pqWDAUt9f0QciCrYLOVrHHgg4hE6MSEHFvkgJ970NA78SmoJMf@h7f2xYQgmfbdhcyhIQBpH@mMCmQc1GG9YdztUBD0W83tFUxIJlqTppnWSLOCGWRt9b0Vxs4KBb31vui0JS6XsGijzP5jAHB5aEwQnIIdi7HI@DMMAJzrQS0CJXcMlqUCtSAxeoQvqNZ0UDnicMgqhFJA/CTEobBnGe03QVchGZPSkpKQWFnwO2A0WUBz0SwBr@xOkKf7Ii@GIVetbtQbwq1Tlue5qOriQVT0H@pa3kB3JLJAuvFPm@gYLwsiQlUjtKjwpOLUVH3llaZsNRfziPjoxrYrBk7xRzl7NWw5hOtdlhdplZROAQoAdPMGuEQo2UM/TDThwxrtM2jwtOrUJTIBiIcg2JHGqnxWPuiM9u53I3YZoMbW9FK4r5dtNdVkRve66JNN3vaBGLillunsuaNIy6B89Knqs2jLbz6Ghx2x2O5tHfMgPid2gBLHyzwzGHDk@XWXXZ8e4FAjGRijFHR76jVyZtVYVSoBKpyD7SkPdsEsMo2dPyygWv7J50BSqtzHiWrugnuDZhYxfzLewN7@4wDa1I1Gd9fU8ozeQ7gqLS/bxgqQiDDyK4OQSRLhzdJcEgiByawE7e@6XYU1zEgmlUgv5DoZ3WJt@mSPlaJXGfSuJ6CzMQxV6@A5q02XB@zJskn/@uIUSpIx0ekA4xinRNorZmD/ST3eEjV0XUiPsgOnyAkAsQ6qUOola0KqsGR1YZeh0aeuRgYkhvIaqj7YbHFI@Wmdj4TFSAJs0R0oCphU4VdOpAX5@FYmA7nIAtOrZhaYWlY4qAhYMIQZhETlCcTJiYDwVliXpbzgXB6C0T2/Jp6VtUiXTqpjHtdMq5sb0s5aatMDV51A7oZmtzutal6jnCbJK2u2jq@bqIrkkbSI0rk2cv7XNlfYYqt0r1@/oSihSe6Wet0cuKskVN2gz7T1V/K8jRQZNWsPrSaUadrJ5maPvbpsar6VVeTa/3avoPePVt7lv3EnH/K7yEm0Tb8689@cGV5XJxWr3822Xy//fINZnSfHHV/NmYtoFe9TVz/ffMBV806pCTYb0ihZ77C6CIGSDuPy1pLjtFwa9pQZfZOmV/0hXcDpSO9J0Dl5KPDUeW5nts7eK42sOUi@o/P0zcdjA2fEKeFYKuHKMBAOfoRmq57GN/w0yrfQDFwJv7twOQ2sXC4iKFYwgo4nRNw9c3N6gfOwq6AzAmX5nvLTe4LZ357Wuf6X5KiTMgp7OAS/2t6ScYBU5DobbL4IZr69RGxzo0285P31/byr/wKqwmrJVGQd3LwpRC2wQ4SoGfYTcmIt6LLMnWj68wl3Iim6XIBlJhGt6yq279ziVpObm7U53VrWmxVnw6TNSnpzB8Zx@495EdvnOGfwE)

# Input

Keywords are `implies`, `and`, `or`, `not`.

Parentheses are not needed unless necessary.

`implies` is right-associative and has the lowest precedence, followed by `or`, and then by `and`, and finally by `not`.

# Examples

For `((P implies Q) implies P) implies P`, it generates the following proof:

```
If not ( P or not P ):
	If P:
		P or not P.
		not ( P or not P ).
		False.
	not P.
	P or not P.
	False.
not not ( P or not P ).
P or not P.
If not ( Q or not Q ):
	If Q:
		Q or not Q.
		not ( Q or not Q ).
		False.
	not Q.
	Q or not Q.
	False.
not not ( Q or not Q ).
Q or not Q.
If P:
	If Q:
		P.
		Q.
		If P:
			Q.
		P implies Q.
		P.
		If P implies Q:
			P.
		( P implies Q ) implies P.
		P.
		If ( P implies Q ) implies P:
			P.
		( ( P implies Q ) implies P ) implies P.
	If not Q:
		P.
		not Q.
		If P implies Q:
			P.
			Q.
			not Q.
			False.
		not ( P implies Q ).
		P.
		If P implies Q:
			If not P:
				P implies Q.
				not ( P implies Q ).
				False.
			not not P.
			P.
		( P implies Q ) implies P.
		P.
		If ( P implies Q ) implies P:
			P.
		( ( P implies Q ) implies P ) implies P.
	( ( P implies Q ) implies P ) implies P.
If not P:
	If Q:
		not P.
		Q.
		If P:
			If not Q:
				P.
				not P.
				False.
			not not Q.
			Q.
		P implies Q.
		not P.
		If ( P implies Q ) implies P:
			P implies Q.
			P.
			not P.
			False.
		not ( ( P implies Q ) implies P ).
		not P.
		If ( P implies Q ) implies P:
			If not P:
				( P implies Q ) implies P.
				not ( ( P implies Q ) implies P ).
				False.
			not not P.
			P.
		( ( P implies Q ) implies P ) implies P.
	If not Q:
		not P.
		not Q.
		If P:
			If not Q:
				P.
				not P.
				False.
			not not Q.
			Q.
		P implies Q.
		not P.
		If ( P implies Q ) implies P:
			P implies Q.
			P.
			not P.
			False.
		not ( ( P implies Q ) implies P ).
		not P.
		If ( P implies Q ) implies P:
			If not P:
				( P implies Q ) implies P.
				not ( ( P implies Q ) implies P ).
				False.
			not not P.
			P.
		( ( P implies Q ) implies P ) implies P.
	( ( P implies Q ) implies P ) implies P.
( ( P implies Q ) implies P ) implies P.
```
