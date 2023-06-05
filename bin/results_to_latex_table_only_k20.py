#!/usr/bin/env python

import sys

before = r"""
\begin{table}
  \centering
  \renewcommand{\arraystretch}{2}
  \setlength{\arrayrulewidth}{0.5mm}
  \begin{tabularx}{\textwidth}{cccc|ccccc}
    \multicolumn{4}{c|}{\textbf{Parametrii de intrare}} & \multicolumn{5}{c}{\textbf{Modele de regresie}} \\
    \cline{0-8}
    % Parameters.
    \rowcolor{gray!25}
"""

def columns(row: list[str]) -> str:
    return """
        \\multicolumn{{1}}{{c}}{{\\textbf{{{0}}}}}
        & \\multicolumn{{1}}{{c}}{{\\textbf{{{1}}}}}
        & \\multicolumn{{1}}{{c}}{{\\textbf{{{4}}}}}
        & \\multicolumn{{1}}{{c|}}{{\\textbf{{{5}}}}}
        % Models.
        & \\multicolumn{{1}}{{c}}{{\\textbf{{{6}}}}}
        & \\multicolumn{{1}}{{c}}{{\\textbf{{{7}}}}}
        & \\multicolumn{{1}}{{c}}{{\\textbf{{{8}}}}}
        & \\multicolumn{{1}}{{c}}{{\\textbf{{{9}}}}}
        & \\multicolumn{{1}}{{c}}{{\\textbf{{{10}}}}} \\\\
        \\cline{{0-8}}
    """.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
               row[8], row[9], row[10])

def data(row: list[str]) -> str:
    return """
        {0} & {1} & {4} & {5}
        & {6}
        & {7}
        & {8}
        & {9}
        & {10} \\\\
    """.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
               row[8], row[9], row[10])

after = r"""
  \end{tabularx}

  \caption{changeme}
  \label{tab:changeme}
\end{table}
"""

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    rows: list[list[str]] = []

    with open(input_file, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        rows = [line.split(',') for line in lines]
        rows = [[col[:8] for col in row] for row in rows]

    header = rows[0]
    rows = rows[1:11]

    with open(output_file, 'w') as f:
        f.write(before)

        f.write(columns(header))
        for row in rows:
            f.write(data(row))

        f.write(after)

if __name__ == '__main__':
    main()
