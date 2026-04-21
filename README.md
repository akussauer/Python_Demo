# UV Demo: Visualizing different package versions

This project demonstrates why **UV** is essential for reproducibility in Python.

- If you run the script, it will print the version of the pandas package being used in the environment that you have selected.
- A project with an UV environment will automatically use the included virtual environment (VENV).
- This ensures that your analysis is reproducible, regardless of the system or Python version you are using.
- If you run the file on its own without the VENV, it will use the system's default Python environment (which may not have the same package versions).