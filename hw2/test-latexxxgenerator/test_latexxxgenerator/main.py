from latexxxgenerator import generate_table, generate_image
import subprocess

table = generate_table([
    ["Name", "Score", "Nickname"],
    ["Inav", 95, "hacker3000"],
    ["Andrey", 88, "booler"],
    ["Alexandr", 15, "winner"],
])

image = generate_image("image.png")

latex = f"""
\\documentclass{{article}}
\\usepackage{{graphicx}}
\\begin{{document}}

{table}

\\bigskip

{image}

\\end{{document}}
"""

with open("output.tex", "w") as f:
    f.write(latex)

subprocess.run(
    ["pdflatex", "output.tex"],
    check=True
)
