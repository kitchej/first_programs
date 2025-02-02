#!/bin/bash
#I, Joshua Kitchen, affirm that I am the sole author if this script, it is my own original work
#March 26, 2021
#Version 1.0

number=$(( 1 + $RANDOM % 100 ))
num_guesses=0

while [[ $guess -ne $number ]]; do
	read -p "Guess a number between 1 and 100: " guess
	num_guesses=$(( $num_guesses + 1 ))
	if [ $guess -gt $number ]; then
		echo "Guess is too high."
	fi
	if [ $guess -lt $number ]; then
		echo "Guess is too low."
	fi
	if [ $guess -eq $number ]; then
		echo "You guessed the number!"
		echo "It took you ${num_guesses} tires"
	fi
done
exit $num_guesses

