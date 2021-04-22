# CS 224 Minesweeper
## Emily Lim

### How To Run:
- cd into directory with the files "main.py", "MineWindow.py", and "MineModel.py".
- Run "python3 main.py" in the terminal.

### Bonus Points Implementations:
#### Allows user to flag bombs by pressing the "Flag" button.
- In flag mode, flag button is green and buttons on grid can be clicked to be flagged.
- To unflag, click the button again and it is reset back to gray.
- Flag mode is off when flag button is clicked again and gray.
- Flags can't be clicked outside of flag mode.

#### Keeps track of number of moves player has made.
- Counter is in the label "Moves Made".