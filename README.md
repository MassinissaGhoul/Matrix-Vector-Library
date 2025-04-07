# Matrix-Vector Library - Test Interface

This project provides an interactive interface to test two main functionalities from a matrix and vector computation library:

- **Pivot Operation**: Apply the pivot operation on an augmented matrix.
- **Simplex Algorithm**: Solve linear programming problems by maximizing an objective function under given constraints.

---

## Prerequisites

- **Python 3.x**: Make sure Python 3 is installed on your system.
- **Required Modules**:  
  The following files must be present inside the `src/` directory:
  - `Matrix.py` – Contains the `Matrix` class with methods such as `pivot` and `simplex`.
  - `Vector.py` – Contains the `Vector` class.

---

## Installation

1. **Clone/Download the Project**  
   Clone the repository or download the following files:

   - `requirements.txt` (located in the root directory)
   - The `src/` directory containing:
     - `interface.py` (the main script)
     - `Matrix.py` (defines the Matrix class)
     - `Vector.py` (defines the Vector class)
     - `testMatrix.py` and `testVector.py` (testing scripts for Matrix and Vector)

2. **Install Dependencies**  
   Open a terminal, navigate to the root directory of the project, and run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Directory Structure**  
   Your project directory should look like this:
   ```
   /root
   ├── requirements.txt
   └── src
       ├── interface.py
       ├── Matrix.py
       ├── Vector.py
       ├── testMatrix.py
       └── testVector.py
   ```

---

## Execution

### Running the Test Interface

To launch the interactive test interface, open a terminal, navigate to the root directory, and run:

```bash
python src/interface.py
```

The menu will display several options:

- **1. Test the Pivot Operation**
- **2. Test the Simplex Algorithm**
- **3. Quit**

Select the desired option by entering the corresponding number.

### Running the Test Scripts

You can also execute the test scripts individually to verify the functionality of the Matrix and Vector classes:

- To test the **Matrix** class:
  ```bash
  python src/testMatrix.py
  ```
- To test the **Vector** class:
  ```bash
  python src/testVector.py
  ```

---

## Features

### 1. Pivot Operation Test

- **Description**:  
  This option allows you to test the pivot operation on an augmented matrix.
- **Usage Modes**:

  - **Example Matrix**: Uses a predefined matrix to demonstrate the pivot operation.
  - **Custom Input**: Allows you to enter your own matrix (dimensions and values).

- **Process**:
  1. Choose the mode (example or custom).
  2. Enter the dimensions and values if using custom input.
  3. Specify the pivot row and column indices (0-indexed).
  4. View the matrix after the pivot operation.

### 2. Simplex Algorithm Test

- **Description**:  
  This option solves a linear programming problem in the standard form:

  - Maximize `z = c^T x`
  - Subject to `Ax <= b` and `x >= 0`

- **Process**:
  1. Enter the number of constraints (`m`) and the number of original variables (`n`).
  2. Input the matrix `A` (row by row).
  3. Input the vector `b` (constraints).
  4. Input the vector `c` (objective function).
  5. Compute and display the optimal solution and its value.

### Menu Navigation

- **Option 1**: Launches the pivot operation test.
- **Option 2**: Launches the simplex algorithm test.
- **Option 3**: Exits the interface.

---
