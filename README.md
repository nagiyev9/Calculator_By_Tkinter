# Calculator Application

This is a Python-based graphical calculator application built using the `tkinter` library along with `ttkbootstrap` for a modern user interface. The calculator supports basic arithmetic operations and additional features like percentage calculation and square operations.

## Features
- Addition, subtraction, multiplication, and division
- Percentage calculation
- Square power calculation
- Clear input

## Prerequisites
Ensure you have the following installed on your system:

- Python 3.x
- Required Python libraries:
  - `ttkbootstrap`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/nagiyev9/Calculator_By_Tkinter.git
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install ttkbootstrap
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Use the on-screen buttons or your keyboard to perform calculations.

## Code Structure

- **`App` Class:** Contains the logic and layout for the calculator application.
- **Buttons:** Each button is assigned a specific function.
  - Numeric and operation buttons input their respective values into the entry field.
  - The `=` button evaluates the entered expression.
  - The `AC` button clears the entry field.

## Notes

- The `x²` button calculates the power of a number, where the base and exponent must be provided (e.g., `2x²3` results in `2^3 = 8`).
- Errors in syntax or invalid input will display an "Error" message in the entry field.

## Troubleshooting

- Ensure you have installed all required dependencies.
- If the application window doesn't display correctly, verify your `ttkbootstrap` installation or try reinstalling it.

## Screenshots

(Include screenshots of the application if possible for better visualization.)

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

---

Enjoy using the calculator application! 🎉
