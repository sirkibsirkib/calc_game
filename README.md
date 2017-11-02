# calc_game

This is a small project to create levels for the android game "Calculator: The Game". I am not affiliated with it, it just provides an interesting challenge and opportunity for me to brush up on my python.

The user can tweak a couple values:
* The starting number
* The max number of operations the user can make
* The set of allowed "operations" (represented in the game as buttons)

Then the user can run the script and it will print out the reachable solutions. Each of these presents:
* The number reached
* The sequence of operations performed to reach it

Eg: starting from 10 with operations [+4, /2] one might see: `[+4, /2] => 7`

This can be used to create new levels easily for the game, as well as provide you with the set of buttons the user would need.
