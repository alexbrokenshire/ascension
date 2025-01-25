import pandas as pd

"""
bivar_truth_table()
This function is used to return a truth table. It has a single parameter 
'selection', which you can pass a list or value to to select the particular 
connective expressions to display.
"""
def display_bivariate_truth_table(selection = None):
    #if (not selection == None) and (any(val == 'p' or val == 'q' for val in selection)):
    #    raise ValueError("Do not provide 'p' or 'q' in selection parameter")
    values = [(False, False), (False, True), (True, False), (True, True)]
    df = pd.DataFrame({
        # Distributions:
        'p': [p for p, q in values],
        'q': [q for p, q in values],
        # Negations:
        '¬p': [not p for p, q in values],
        '¬q': [not q for p, q in values],
        # Conjunctions:
        'p ∧ q': [p and q for p, q in values],
        '¬p ∧ q': [not p and q for p, q in values],
        'p ∧ ¬q': [p and not q for p, q in values],
        '¬p ∧ ¬q': [not p and not q for p, q in values],
        # Negated conjunctions:
        '¬(p ∧ q)': [not (p and q) for p, q in values],
        '¬(¬p ∧ q)': [not (not p and q) for p, q in values],
        '¬(p ∧ ¬q)': [not(p and not q) for p, q in values],
        '¬(¬p ∧ ¬q)': [not(not p and not q) for p, q in values],
        # Converse conjunctions:
        'q ∧ p': [q and p for p, q in values],
        '¬q ∧ p': [not q and p for p, q in values],
        'q ∧ ¬p': [q and not p for p, q in values],
        '¬q ∧ ¬p': [not q and not p for p, q in values],
        # Converse negated conjunctions:
        '¬(q ∧ p)': [not(q and p) for p, q in values],
        '¬(¬q ∧ p)': [not(not q and p) for p, q in values],
        '¬(q ∧ ¬p)': [not(q and not p) for p, q in values],
        '¬(¬q ∧ ¬p)': [not(not q and not p) for p, q in values],
        # Disjunctions:
        'p ∨ q': [p or q for p, q in values],
        '¬p ∨ q': [not p or q for p, q in values],
        'p ∨ ¬q': [p or not q for p, q in values],
        '¬p ∨ ¬q': [not p or not q for p, q in values],
        # Negated disjunctions:
        '¬(p ∨ q)': [not(p or q) for p, q in values],
        '¬(¬p ∨ q)': [not(not p or q) for p, q in values],
        '¬(p ∨ ¬q)': [not(p or not q) for p, q in values],
        '¬(¬p ∨ ¬q)': [not(not p or not q) for p, q in values],
        # Converse disjunctions:
        'q ∨ p': [q or p for p, q in values],
        '¬q ∨ p': [not q or p for p, q in values],
        'q ∨ ¬p': [q or not p for p, q in values],
        '¬q ∨ ¬p': [not q or not p for p, q in values],
        # Converse negated disjunctions:
        '¬(q ∨ p)': [not(q or p) for p, q in values],
        '¬(¬q ∨ p)': [not(not q or p) for p, q in values],
        '¬(q ∨ ¬p)': [not(q or not p) for p, q in values],
        '¬(¬q ∨ ¬p)': [not(not q or not p) for p, q in values],
        # Implications:
        'p → q': [not p or q for p, q in values],
        '¬p → q': [p or q for p, q in values],
        'p → ¬q': [not p or not q for p, q in values],
        '¬p → ¬q': [p or not q for p, q in values],
        # Negated implications (inverse?)
        '¬(p → q)': [not(not p or q) for p, q in values],
        '¬(¬p → q)': [not(p or q) for p, q in values],
        '¬(p → ¬q)': [not(not p or not q) for p, q in values],
        '¬(¬p → ¬q)': [not(p or not q) for p, q in values],
        # Converse implications
        'q → p': [not q or p for p, q in values],
        '¬q → p': [q or p for p, q in values],
        'q → ¬p': [not q or not p for p, q in values],
        '¬q → ¬p': [q or not p for p, q in values],
        # Negated converse implications
        '¬(q → p)': [not(not q or p) for p, q in values],
        '¬(¬q → p)': [not(q or p) for p, q in values],
        '¬(q → ¬p)': [not(not q or not p) for p, q in values],
        '¬(¬q → ¬p)': [not(q or not p) for p, q in values],
        # Biconditionals
        'p ↔ q': [(p == q) for p, q in values],
        '¬p ↔ q': [((not p) == q) for p, q in values],
        'p ↔ ¬q': [((not q) == p) for p, q in values],
        '¬p ↔ ¬q': [((not p) == (not q)) for p, q in values],
        '¬(p ↔ q)': [not(p == q) for p, q in values],
        '¬(¬p ↔ q)': [not((not p) == q) for p, q in values],
        '¬(p ↔ ¬q)': [not((not q) == p) for p, q in values],
        '¬(¬p ↔ ¬q)': [not((not p) == (not q)) for p, q in values],
        # Converse biconditionals:
        'q ↔ p': [(q == p) for p, q in values],
        '¬q ↔ p': [((not q) == p) for p, q in values],
        'q ↔ ¬p': [((not p) == q) for p, q in values],
        '¬q ↔ ¬p': [((not q) == (not p)) for p, q in values],
        '¬(q ↔ p)': [not(q == p) for p, q in values],
        '¬(¬q ↔ p)': [not((not q) == p) for p, q in values],
        '¬(q ↔ ¬p)': [not((not p) == q) for p, q in values],
        '¬(¬q ↔ ¬p)': [not((not q) == (not p)) for p, q in values]
    })

    # If no selection, just return the propositional variables, otherwise
    # return the propositional variables and the selection
    if selection == None:
        df = df[['p','q']]
    else:
        if isinstance(selection, str): 
            selection = [selection]
        df = df[['p', 'q'] + selection]

    # Define a formatting rule to apply to all of the interior cells:
    def format_cell(val):
        background_color = 'lightgreen' if val else 'lightpink'
        text_color = 'green' if val else 'red'
        return f'background-color: {background_color}; color: {text_color}'

    df = df.style.applymap(format_cell)

    # Set table styles:
    df = df.set_table_styles([
        # Header:
        {
            'selector': 'th', 
            'props': [
                ('background-color', 'black'),
                ('color', 'white'),
                ('text-align', 'center')
            ]
        },
        # Cells:
        {
            'selector': 'td',
            'props': [
                ('text-align', 'center') 
            ]
        }
        ], axis = 1).hide(axis = "index")

    # Return the data frame with the desired columns and formatting:
    return df