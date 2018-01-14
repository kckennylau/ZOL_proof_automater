This is an automater for proofs in zeroth-order logic (propositional logic).

It can prove every tautology, and it will error when given a statement that is not a tautology.

It operates under classical logic, and proceeds via what is essentially the semantic-completeness theorem.

First, it proves an instance of LEM for every variable that it encounters.

Then, it uses disjunction elimination and separates into as many cases as two to the power of the number of variables, and proves the theorem in each case by building up from the inside to the outside.

This is also my first attempt at writing a parser.
