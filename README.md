##  **How to Run the Code**

1. **Save the script**
   Copy the code I gave you into a file called `calculator.py`.

2. **Open Terminal / Command Prompt**

   * If you are using **VS Code**, open the built-in terminal.
   * Navigate to the folder where you saved `calculator.py` (use `cd folder_name`).

3. **Run the Program**
   Type:
   python calculator.py

4. **Use the Calculator**

   * Enter an operator (`+`, `-`, `*`, `/`)
   * Enter two numbers
   * Get the result
   * Type `exit` anytime to stop the program.



## Explanation of the Code

1. **Functions for Each Operation**

   * `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)`
   * Each function performs only **one specific job** → makes the code clean and reusable.
   * Example: `add(5, 3)` → returns `8`.

2. **Main Loop (`while True`)**

   * Keeps the calculator running until the user types `"exit"`.
   * This makes it a **command-line app** instead of a one-time calculator.

3. **Operator Input**

   * Program asks the user to enter which operation (`+ - * /`) they want.
   * If user types something invalid, it prints an error and restarts.

4. **Number Inputs**

   * User enters two numbers (`float` allows decimals).
   * Code checks if inputs are valid, otherwise shows `"Invalid input!"`.

5. **Performing Calculations**

   * Based on the operator, the correct function is called.
   * Example: if user entered `"*"`, program runs `multiply(num1, num2)`.

6. **Division Error Handling**

   * If user tries to divide by zero, function returns `"Error: Division by zero"` instead of crashing.

7. **Exit Option**

   * If user types `"exit"`, the loop breaks and program ends with `"Goodbye"
