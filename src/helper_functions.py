import pandas as pd

"""
bivar_truth_table()
This function is used to return a truth table. It has a single parameter 
'selection', which you can pass a list or value to to select
"""
def display_bivariate_truth_table(selection = None):
    #if (not selection == None) and (any(val == 'p' or val == 'q' for val in selection)):
    #    raise ValueError("Do not provide 'p' or 'q' in selection parameter")
    values = [(False, False), (False, True), (True, False), (True, True)]
    df = pd.DataFrame({
        'p': [p for p, q in values],
        'q': [q for p, q in values],
        '¬p': [not p for p, q in values],
        '¬q': [not q for p, q in values],
        'p ∧ q': [p and q for p, q in values],
        'p ∨ q': [p or q for p, q in values],
        'p → q': [not p or q for p, q in values],
        'p ↔ q': [(p == q) for p, q in values],
    })

    if selection == None:
        df = df[['p','q']]
    else:
        if isinstance(selection, str): 
            selection = [selection]
        df = df[['p', 'q'] + selection]

    def format_cell(val):
        background_color = 'lightgreen' if val else 'lightpink'
        text_color = 'green' if val else 'red'
        return f'background-color: {background_color}; color: {text_color}'
    
    df = df.style.applymap(format_cell)
    df = df.set_table_styles([
        {
            'selector': 'th', 
            'props': [
                ('background-color', 'black'),
                ('color', 'white'),
                ('text-align', 'center')
            ]
        }], axis = 1).hide(axis = "index")

    
    return df