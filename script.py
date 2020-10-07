def f(n):
    '''
    Formats an integer to a string with comma separation.
    Example:
        1000000 => "1,000,000"
    '''
    return '{:,}'.format(n)

# read text file copied from wikipedia
with open("population.txt") as file:
    content = file.read().strip()
    lines = content.split("\n")
    pop_cells = [x.split("\t") for x in lines]

# for each row in the table, add to dictionary with (state, population)
pops = {}
for row in pop_cells:
    state = row[2].strip().lower()
    pop = int(row[3].strip().replace(',', ''))
    
    pops[state] = pop


# read the html file for the election results page
with open("results.html") as file:
    results_content = file.read().strip()
    res_lines = results_content.split('\n')

# read through the lines
# lines with states were formatted as: "Alabama</a>"
# so the "</a>" has to be removed for proper name
# after each state the next line with "Winner" has the name of the winning candidate
# add to dictionary with (state, "D") if democrat won or (state, "R")
results = {}
for line in res_lines:
    if "</a>" in line:
        line = line[:line.index("</a>")]
    if line.lower() in pops:
        state = line.strip().lower()

    if "Winner" in line:
        if "clinton" in line.lower():
            results[state] = "D"
        elif "trump" in line.lower():
            results[state] = "R"

# print(pops)
# print(results)


# Iterate through each state and add up the total population for both groups
d_total = 0
r_total = 0
total_population = 0
state_total = 0
for state in results:
    total_population += pops[state]
    state_total += 1
    if results[state] == "D":
        d_total += pops[state]
    elif results[state] == "R":
        r_total += pops[state]


# Print out the results
print(f"Total Population of Republican won states: {f(r_total)}")
print(f"  Total Population of Democrat won states: {f(d_total)}")
print(f"\n                  Total voting population: {f(total_population)}")
print(f"                   Total number of states: {state_total}")
