% ============================================================
% Experiment 2C - Query Execution (simple clauses in Prolog)
% Course : AI23231 - Principles of Artificial Intelligence Lab
%
% Aim    : To represent knowledge as facts and rules in Prolog and
%          execute queries against it.
%
% Run    : swipl 2C_prolog_queries.pl
%          then type the queries below at the  ?-  prompt.
%          Press ';' to see further answers, '.' to stop.
% ============================================================

% ---------------- Facts ----------------
likes(mary, food).
likes(mary, wine).
likes(john, wine).
likes(john, mary).

% ---------------- Rules ----------------
% 1. John likes anything that Mary likes.
likes(john, X) :- likes(mary, X).
% 2. John likes anyone who likes wine.
likes(john, Y) :- likes(Y, wine).
% 3. John likes anyone who likes themselves.
likes(john, Y) :- likes(Y, Y).

% ------------------------------------------------------------
% Queries
% ------------------------------------------------------------
% With ONLY the four facts above (rules removed), the answers are:
%   ?- likes(mary, food).   -> true   (yes)
%   ?- likes(john, wine).   -> true   (yes)
%   ?- likes(john, food).   -> false  (no)
%
% With the three rules added:
%   ?- likes(john, food).   -> true.   (rule 1: Mary likes food)
%   ?- likes(john, wine).   -> true.   (fact)
%   ?- likes(john, Y).
%        Y = wine ;         (fact)
%        Y = mary ;         (fact)
%        Y = food ;         (rule 1)
%        Y = wine ;         (rule 1)
%        Y = mary ;         (rule 2: mary likes wine)
%        Y = john ;         (rule 2: john likes wine)
%        ...                (answers can repeat: Prolog reports every proof)
%
% Note: rule 3 can make a search with an unbound variable run for a long
% time or loop when you keep pressing ';'. Stop with '.' or Ctrl+C.
