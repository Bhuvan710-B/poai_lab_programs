% Experiment 2A: Introduction to Prolog
% Minimum, maximum, and likes predicates from the lab manual.

% Find the minimum of two numbers.
minimum(X, Y, X) :- X =< Y.
minimum(X, Y, Y) :- X > Y.

% Find the maximum of two numbers.
maximum(X, Y, X) :- X >= Y.
maximum(X, Y, Y) :- X < Y.

% Given facts.
likes(mary, food).
likes(mary, wine).
likes(john, wine).
likes(john, mary).

% Rules from the lab manual.
likes(john, X) :- likes(mary, X).
likes(john, Y) :- likes(Y, wine).
likes(john, Y) :- likes(Y, Y).

% Example queries (enter these at the Prolog prompt):
% ?- minimum(5, 10, Min).
% ?- maximum(5, 10, Max).
% ?- minimum(8, 3, Min), maximum(8, 3, Max).
% ?- likes(mary, food).
% ?- likes(john, wine).
% ?- likes(john, food).
% ?- likes(john, Y).