import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('coverage.xml')
root = tree.getroot()

# Specify the function name to exclude
function_name = 'my_function'  # Replace with the actual function name

# Initialize coverage counters
total_lines = 0
covered_lines = 0
total_branches = 0
covered_branches = 0
total_functions = 0
covered_functions = 0

# Iterate over each file in the XML
for file in root.findall('file'):
    # Iterate over each function in the file
    functions = file.findall('functions/function')
    for function in functions:
        if function.get('name') == function_name:
            # Gather metrics before removal
            total_functions += 1
            covered_functions += int(function.get('hits') > 0)
            # Remove the function from the XML
            file.remove(function)
        else:
            total_functions += 1
            covered_functions += int(function.get('hits') > 0)

    # Iterate over each line in the file to gather line coverage
    for line in file.findall('lines/line'):
        total_lines += 1
        if int(line.get('hits')) > 0:
            covered_lines += 1
        # If branch coverage is available
        if 'branches' in line.attrib:
            total_branches += 1
            if int(line.get('branches')) > 0:
                covered_branches += 1

# Update overall coverage metrics
line_coverage = (covered_lines / total_lines * 100) if total_lines > 0 else 0
branch_coverage = (covered_branches / total_branches * 100) if total_branches > 0 else 0
function_coverage = (covered_functions / (total_functions - 1) * 100) if total_functions > 1 else 0

# Update the root element with new coverage metrics
root.set('line-rate', f"{line_coverage:.4f}")
root.set('branch-rate', f"{branch_coverage:.4f}")
root.set('function-rate', f"{function_coverage:.4f}")

# Save the modified XML
tree.write('filtered_coverage.xml', encoding='utf-8', xml_declaration=True)

print("Filtered coverage report generated: filtered_coverage.xml")
