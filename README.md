## 🧮 Scientific Calculator (SC)

This project is a scientific calculator application built using Python's **`tkinter`** library for the graphical user interface. It features basic arithmetic operations, common scientific functions, and persistent storage of the last result and user theme.

-----

## ✨ Features

  * **GUI Interface:** User-friendly, desktop-based interface built with `tkinter`.
  * **Basic Arithmetic:** Supports addition (`+`), subtraction (`-`), multiplication (`×`), and division (`÷`).
  * **Scientific Functions:** Includes:
      * Trigonometric functions: **`sin`**, **`cos`**, **`tan`**.
      * Logarithm: **`log`** (natural logarithm, base $e$).
      * Power: **`^`** (e.g., $x^y$).
      * Square Root: **`√`**.
      * Factorial: **`!`** (e.g., $5!$).
      * Constants: **$\pi$** and **$e$**.
  * **Persistent Memory (`Ans`):** The last calculated result is stored and can be recalled into the current expression using the **`Ans`** button.
  * **Settings Persistence:** Saves the last result and the user's preferred theme (light or dark) to a file named `calc_user.settings`.
  * **Themes:** Supports two basic color schemes: **"light"** (default) and **"dark"**.
  * **Error Handling:** Catches and displays messages for invalid expressions (syntax errors, domain errors) during calculation.

-----

## 💻 Dependencies

This application requires only standard Python libraries:

  * **`tkinter`**: For the GUI.
  * **`math`**: For all scientific functions (e.g., `sin`, `sqrt`, `factorial`).
  * **`json`**: For saving and loading settings.
  * **`os`**: For checking file existence.
  * **`re`**: For regular expression parsing (specifically for the factorial operator).

-----

## 🚀 How to Run

1.  **Prerequisites:** Ensure you have Python installed (Python 3.x is recommended). `tkinter` is usually included with standard Python installations.

2.  **Save the Code:** Save the provided code as a Python file (e.g., `calculator.py`).

3.  **Execute:** Run the file from your command line:

    ```bash
    python calculator.py
    ```

-----

## 🛠️ Implementation Details

### Settings File

  * The application creates a file named **`calc_user.settings`** in the same directory as the script.
  * The file uses JSON format to store settings, structured as:
    ```json
    {
        "t": "light",  // Theme: "light" or "dark"
        "l": 0.0       // Last result (Ans)
    }
    ```

### Calculation Engine

The core of the calculator is the **`calc`** method, which safely evaluates the input expression:

1.  It replaces user symbols (`×`, `÷`, `√`, `^`) with Python operators (`*`, `/`, `math.sqrt`, `**`).
2.  It replaces scientific names (e.g., `sin`) with calls to the `math` library (e.g., `math.sin`).
3.  It uses **`eval()`** with a restricted global and local dictionary (`{"__builtins__": None, "math": math}`) to ensure only safe mathematical functions can be executed, preventing the running of arbitrary system commands.
