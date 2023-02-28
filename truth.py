from typing import Callable
from inspect import signature

import rich
from rich.table import Table

def truth_table(f: Callable[..., bool]) -> list[list[bool]]:
    """
    Generate a truth table for a given function.

    Args:
        f (Callable[..., bool]): A function that takes in a variable number of boolean parameters and returns a boolean.

    Returns:
        _type_: Truth table for the given function.
    """
    
    # Get the number of parameters the function takes in.
    number_of_params: int = len(signature(f).parameters)
    
    # Generate the truth table.
    table: list[list[bool]] = []
    
    # Iterate through all possible combinations of boolean values.
    for i in range(2 ** number_of_params):
        # Convert the current number to a binary string, pad it with 0s to the left, and convert it to a list of booleans.
        row: list[bool] = [bool(int(x)) for x in bin(i)[2:].zfill(number_of_params)]
        # Append the result of the function to the row.
        table.append(row + [f(*row)])
    
    # Return the truth table.
    return table
    
def pretty_print(table: list[list[bool]], columns: list[str] | None = None, 
                 row_no: bool = True,
                 title: str | None = None,
                 rep_true: str = "True",
                 rep_false: str = "False") -> None:
    """
    Print a truth table in a nice format.

    Args:
        table (list[list[bool]]): Truth table to print.
    """
    
    _table: Table = Table(show_header=True, header_style="bold")
    
    _table.title = title
    
    if columns is None:
        columns = [f"x{i}" for i in range(len(table[0]) - 1)] + ["f"]
        
        if row_no:
            columns = ["#"] + columns
    
    for column in columns:
        _table.add_column(column, justify="center")
        
    for i, row in enumerate(table):
        if row_no:
            _table.add_row(str(i), *[rep_true if x else rep_false for x in row])
        else:
            _table.add_row(*[rep_true if x else rep_false for x in row])
        
    rich.print(_table)