import subprocess

steps = [
    "python INEI-Education\scripts\\extract.py",
    "python INEI-Education\scripts\\transform.py",
    "python INEI-Education\scripts\\load.py"
]

for step in steps:
    print(f"Running: {step}")
    result = subprocess.run(step, shell=True)

    if result.returncode != 0:
        print(f"Error in step: {step}.")
        break
    else:
        print("Step {step} completed.")