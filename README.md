# Dice Simulation and Visualization

This repository demonstrates Python-based simulations of dice rolls and their visualization using the `pygal` library.

## Project Structure

- `die.py`: A Python class representing a single die, which can have a custom number of faces.
- `Die_visual.py`: A script that rolls a single 6-sided die 1000 times and visualizes the results as a bar chart.
- `Die_visual2.py`: A script that rolls two 6-sided dice 1000 times, computes the sum of the rolls, and visualizes the results as a bar chart.
- `Die_visual3.py`: A script that rolls a 6-sided and a 10-sided dice 1000 times, computes the sum of the rolls, and visualizes the results as a bar chart.
- `die_visual.svg`: The output visualization for rolling a single die.
- `die_visual2.svg`: The output visualization for rolling two dice.
- `die_visual3.svg`: The output visualization for rolling two dice.

## Details

### `die.py`
Defines the `Die` class with the following features:
- **Attributes**:
  - `faces`: The number of faces on the die (default is 6).
- **Methods**:
  - `Roll()`: Returns a random value between 1 and the number of faces.
Die_visual.py
Simulates rolling a single die 1000 times and generates a bar chart visualization.

###`die_visual.py`
Simulates rolling a single die 1000 times and generates a bar chart visualization.

**Key Steps**:
- Rolls a 6-sided die 1000 times using the Die class.
- Records the frequency of each outcome (1 to 6).
- Visualizes the results as a bar chart saved to die_visual.svg.

## Requirements
- Python 3.x
- **Libraries:**
   - pygal
   - random (standard Python library)
   
Install `pygal` using pip:

>`pip install pygal`

##How to run:
- Clone this repository.
- make changes to die object for different number of die faces bar charts like blow example in `die_visual.py`
```
die_1=Die()
die_2=Die(10)
```
- run the code.
- open the respective `.svg` file

## Output Visualization

### Single 6-Faced Die Roll Visualization
  
![die_visual](https://github.com/user-attachments/assets/306cfbc8-da4d-45bf-b286-b37926504761)

### Double 6-faced Die Roll Visualization
![die_visual2](https://github.com/user-attachments/assets/f4609d1a-08b1-409a-895b-f065e6669122)

### A 6-faced and a 10-faced Die Roll Visualization
![die_visual3](https://github.com/user-attachments/assets/d2759bfd-9eff-4954-88e2-1c151c9704c1)



