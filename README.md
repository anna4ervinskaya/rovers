# Mars Rover technical Challenge

This programm based on data of initial positions and movement commands for rovers returns terminates positions for each of them.

## Installation & Run
```bash
# Download this project
git clone https://github.com/anna4ervinskaya/rovers/
# Run
cd rovers
python -m main input.txt
```
## Testing
```bash
# Run all tests
python -m unittest discover
# Run specific test
python -m unittest tests.test_main
```
## Structure
``` 
|   input.txt                             // Sample data for rovers
|   main.py                               // Main module for getting result data
|   rover.py                              // Module describes rover class
|   rover_controller.py                   // Module describes rover controller class
└── tests                                 // Folder for test
    |   test_main                         // Test module for main function
    |   test_rover                        // Test modulefor rover
    |   test_rover_controller             // Test module for controller
    └── fixtures                          // Folder for tests data
        |   input_correct.txt             // Correct data
        |   input_incorrect_commands.txt  // Incorrect commands data
        |   input_incorrect_plateau.txt   // Incorrect plateau limits data
        └── input_incorrect_position.txt  // Data for rovers paths clash
```

## Input data rules
Input file should contains these data:
- First line for upper right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0. It consists of two positive numbers divided by space. If it does not fit this pattern the program will gives an error ValueError('Plateau limits data is not correct')
``` 
6 6
``` 
- Second line for initial position of a rover. It consists of two positive numbers and one capital letter (N/W/S/E) for rover's orientation, every parameter divided by spaces. If it does not fit this pattern the program will give an error ValueError('Rover position data is not correct')
``` 
5 4 N
```
- Third line is a series of instructions telling the rover how to explore the plateau, wich consists of capital letters. The possible letters are 'L', 'R' and 'M'. If it does not fit this pattern the program will give an error ValueError('Rover commands data is not correct')
``` 
LMLMLMLMM
```
