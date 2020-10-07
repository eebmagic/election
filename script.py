def f(n):
    return '{:,}'.format(n)

with open("population.txt") as file:
    content = file.read().strip()

lines = content.split("\n")
cells = [x.split("\t") for x in lines]

pops = {}
for row in cells:
    state = row[2].strip().lower()
    pop = int(row[3].strip().replace(',', ''))
    
    pops[state] = pop


with open("results.html") as file:
    results_content = file.read().strip()

results = {}
res_lines = results_content.split('\n')
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


print(f"Total Population of Republican won states: {f(r_total)}")
print(f"  Total Population of Democrat won states: {f(d_total)}")
print(f"\n                  Total voting population: {f(total_population)}")
print(f"                   Total number of states: {state_total}")