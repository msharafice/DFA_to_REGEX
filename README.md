# DFA to REGEX

## Project Description
This project converts a Deterministic Finite Automaton (DFA) into a Regular Expression (REGEX). The DFA is represented as a set of state transitions, and the corresponding regular expression is generated based on these transitions.

## Features
- Converts DFA state transitions to a regular expression.
- Handles any DFA with multiple states and input symbols.
- Supports both basic and complex DFA structures.

## Input Format
The input for this project follows the format below:

- The state transitions are defined in the form `(state, symbol) = next_state`, where `state` is the current state, `symbol` is the input symbol, and `next_state` is the state reached after processing the symbol.

Example:
(1,a)=2 (2,b)=3 (3,c)=4 (4,c)=4 (4,a)=2
 
final_state=[4]

initial_state=1

user_input_string=abcabc


## Output Format
The output will be the regular expression corresponding to the DFA. It will be followed by a message indicating whether the input string is accepted by the DFA.

Example output:

#REGEX

(a)*

string accepted


