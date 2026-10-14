% ============================================================
% Experiment 2 (Prolog) - Simple programs: minimum and maximum
%                         of two numbers
% Course : AI23231 - Principles of Artificial Intelligence Lab
%
% Aim    : To find the minimum and maximum of two numbers using
%          Prolog (decision making with rules).
%
% Run    : swipl 2A_prolog_min_max.pl
%          then type the queries below at the  ?-  prompt.
%          (Or non-interactively:
%           swipl -q -g "minimum(5,10,M), writeln(M), halt." 2A_prolog_min_max.pl)
% ============================================================

% minimum(X, Y, Min): Min is the smaller of X and Y.
minimum(X, Y, X) :- X =< Y.   % If X is less than or equal to Y, X is the minimum.
minimum(X, Y, Y) :- X > Y.    % If X is greater than Y, Y is the minimum.

% maximum(X, Y, Max): Max is the larger of X and Y.
maximum(X, Y, X) :- X >= Y.   % If X is greater than or equal to Y, X is the maximum.
maximum(X, Y, Y) :- X < Y.    % If X is less than Y, Y is the maximum.

% ------------------------------------------------------------
% Example queries and their answers
% ------------------------------------------------------------
% ?- minimum(5, 10, Min).
% Min = 5.
%
% ?- maximum(5, 10, Max).
% Max = 10.
%
% ?- minimum(8, 3, Min), maximum(8, 3, Max).
% Min = 3,
% Max = 8.
