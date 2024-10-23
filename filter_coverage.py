from bs4 import BeautifulSoup

# Load the HTML file
with open('coverage.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Function name to remove
function_name = 'my_function'

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
        line_count = int(entry.find_all('td')[1].text)  # Assuming line coverage is in the second <td>
        covered_count = int(entry.find_all('td')[2].text)  # Assuming covered lines are in the third <td>
        total_lines += line_count
        covered_lines += covered_count
        
        # Optionally update branch coverage if available
        if len(entry.find_all('td')) > 3:  # Check if branch coverage exists
            branch_count = int(entry.find_all('td')[3].text)  # Adjust index as necessary
            covered_branch_count = int(entry.find_all('td')[4].text)  # Adjust index as necessary
            total_branches += branch_count
            covered_branches += covered_branch_count

        total_functions += 1  # Assuming we count the removed function
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

# Update the coverage summary
coverage_summary = soup.find('div', class_='summary')
if coverage_summary:
    coverage_summary.find('span', class_='line-coverage').string = f"{line_coverage:.2f}%"
    coverage_summary.find('span', class_='branch-coverage').string = f"{branch_coverage:.2f}%"
    # Update function coverage if applicable
    function_coverage = (covered_functions / (total_functions - 1)) * 100 if total_functions > 1 else 0
    coverage_summary.find('span', class_='function-coverage').string = f"{function_coverage:.2f}%"

# Save the modified HTML
with open('filtered_coverage.html', 'w') as file:
    file.write(str(soup))
