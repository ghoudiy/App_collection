import re

def extract_functions(file_path, pattern):
    with open(file_path, 'r') as f:
        content = f.read()
    return set(re.findall(pattern, content))

# Function patterns
definition_pattern = r'\b\w+\s+\w+\s*\([^)]*\)\s*\{'
declaration_pattern = r'\b\w+\s+\w+\s*\([^)]*\)\s*;'

# File paths
c_file = 'tableau_bord_stocks.c'
h_file = 'tableau_bord_stocks.h'

# Extract functions
c_functions = extract_functions(c_file, definition_pattern)
h_functions = extract_functions(h_file, declaration_pattern)

# print(h_functions)
# Compare and report
for func in c_functions:
    # print("'" + func.replace('{', ";") + "'")
    if func.replace('\n{', ';').replace(" {", ";") not in h_functions:
        print(f"Function missing in header file: '{func}'")
