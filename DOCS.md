# UFO GAME
Invaders from outer space have arrived and are abducting humans using tractor beams. Earn your medal of honor by cracking the codeword to stop the abduction!
<br/>
<br/>

## Setup
As a prerequisite python version 3.6 and above is required. Check your python version by running the following command

    python3 --version
    
## Download the files
Download the files and unzip the contents . Navigate to the project root so that running `ls` shows `main.py` among other files.

## Run the game
In the current folder run the following command to run the python file.

    python3 main.py
The game should start and will load the contents. Happy gaming! 
<br/>
<br/>

## How to play
Guess one letter at a time of a codeword represented by blank placeholders for each letter. If the letter does not exist in the codeword, the person is pulled in closer to the UFO by the tractor beam. If the letter exists, the blanks that correspond to the position of those letters in the codeword are replaced by the letter. If all the letters of the codeword are revealed before the person is pulled into the UFO, you win. Otherwise, the UFO abducts the person and you lose.

## Run the test file
In the current folder run the following command to run the python file.

    python3 user_guess_unittest.py