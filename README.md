# game-of-life
This is a very short code implementation of Conway's Game of Life using Python and the pygame library as a personal exploration into algorithms.

## Game Operation
The game starts paused to allow the user to draw with the left mouse button then when the desired pattern is intialized the user can then begin the game by pressing the unpause button 'P'.
The game surrently runs at 1 FPS to see the changes in  the pattern. Future revisions will include the ability to change this frame rate.

## Inital Set Up
This game uses Numerical Python to generate an 80x60 grid of 10px cells with an assigned value of zero. This is then changed by the user as they click on desired inital states.
THe game uses the pygame library to obtain the mouse position on the display screen, and when the user clicks the mouse button to select a certain cell and determine it's state.
