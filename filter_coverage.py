from bs4 import BeautifulSoup

# Load the HTML file
with open('coverage.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Specify the function name to exclude
function_name = 'my_function'  # Replace with the actual function name

# Initialize coverage counters
total_lines = 0
covered_lines = 0
total_branches = 0
covered_branches = 0
total_functions = 0
covered_functions = 0

# Find and remove function entries
function_entries = soup.find_all('tr')
for entry in function_entries:
    if function_name in entry.text:
        # Update coverage metrics before removing
        cells = entry.find_all('td')
        if len(cells) >= 5:  # Check that there are enough columns
            line_count = int(cells[1].text)  # Total lines (2nd column)
            covered_count = int(cells[2].text)  # Covered lines (3rd column)
            branch_count = int(cells[3].text)  # Total branches (4th column)
            covered_branch_count = int(cells[4].text)  # Covered branches (5th column)

            total_lines += line_count
            covered_lines += covered_count
            total_branches += branch_count
            covered_branches += covered_branch_count
            
        total_functions += 1  # Counting the removed function
        entry.decompose()  # Remove the function entry

# Update overall coverage metrics
if total_lines > 0:
    line_coverage = (covered_lines / total_lines) * 100
else:
    line_coverage = 0

if total_branches > 0:
    branch_coverage = (covered_branches / total_branches) * 100
else:
    branch_coverage = 0

# Function coverage calculation (excluding the removed function)
total_functions = max(total_functions - 1, 1)  # Ensure at least 1 for division
function_coverage = (covered_functions / total_functions) * 100 if total_functions > 0 else 0

# Update the coverage summary in the HTML
coverage_summary = soup.find('div', class_='summary')
if coverage_summary:
    line_coverage_elem = coverage_summary.find('span', class_='line-coverage')
    branch_coverage_elem = coverage_summary.find('span', class_='branch-coverage')
    function_coverage_elem = coverage_summary.find('span', class_='function-coverage')

    if line_coverage_elem:
        line_coverage_elem.string = f"{line_coverage:.2f}%"
    if branch_coverage_elem:
        branch_coverage_elem.string = f"{branch_coverage:.2f}%"
    if function_coverage_elem:
        function_coverage_elem.string = f"{function_coverage:.2f}%"

# Save the modified HTML
with open('filtered_coverage.html', 'w') as file:
    file.write(str(soup))

print("Filtered coverage report generated: filtered_coverage.html")
