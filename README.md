% DFA to REGEX
% This project converts a Deterministic Finite Automaton (DFA) to a Regular Expression (REGEX).

% Short Description:
% This project takes a DFA as input and converts it into a Regular Expression using standard algorithms. 
% It is useful for simplifying DFAs into regular expressions for easier processing.

% Features:
% - Accepts a DFA in the specified format.
% - Converts the DFA into an equivalent regular expression.
% - Checks whether a given input string is accepted by the DFA.
% - Provides the corresponding regular expression for the DFA.

% Input Format:
% The DFA is represented as a set of transitions and a start state.
% Transitions are given in the format (current_state, input_symbol) = next_state.
% The final state(s) are also specified in the final_state array.
% The initial state is indicated by the initial_state variable.
% Example:
% (1,a)=2
% (2,b)=3
% (3,c)=4
% (4,c)=4
% (4,a)=2

final_state=[4];

initial_state=1;

user_input_string='abcabc';

% Output Format:
% The output will include the corresponding regular expression and whether the input string is accepted by the DFA.
% The regular expression for the given DFA will be displayed as well.
% Example:
% #REGEX
% (a)*

% string accepted

% Usage:
% Run the code to convert the DFA into a regular expression and check if the user input string is accepted.
