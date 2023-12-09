import os
import shutil

current_path = os.getcwd()
path_of_new_solutions = current_path + '/new_solutions'
path_of_solved_solutions = current_path + '/solutions'
db = []
readme = []
with open('db.txt', 'r') as f:
    db = [line for line in f]
with open('readme.md', 'r') as f:
    readme = [line for line in f]


# New Solutions
new_solutions = list(os.walk(path_of_new_solutions))[0][2] # list of solutions file names

# Update Solved Count
old_problems_solved_count = int(db[0].split(':')[1])
new_problems_solved_count = old_problems_solved_count + len(new_solutions)
db[0] = f'Problems Solved: {new_problems_solved_count}\n' # updates db count
#print(f"Count updated from {old_problems_solved_count} to {new_problems_solved_count}")

# Update Read Me
e = f"## Problems Solved: {old_problems_solved_count}\n"
i= readme.index(e) if e in readme else -1
if i == -1:
    print("Count mismatch.")
    exit()
readme[i] = f"## Problems Solved: {new_problems_solved_count}\n"

# Move new_solutions to solutions
for s in new_solutions:
    os.mkdir(f'{path_of_solved_solutions}/{s[:-3]}')
    shutil.move(f'{path_of_new_solutions}/{s}', f'{path_of_solved_solutions}/{s[:-3]}/{s}')


# Add new solutions to DB and README variable
for i in new_solutions:
    ref_url = 'https://open.kattis.com/problems/' + i[:-3]
    ans_url = f'https://github.com/sh3ngsh3ng/kattis-python-solutions/tree/main/solutions/' + i[:-3]
    db.append(f"|{i[:-3]}|{ref_url}|{ans_url}|\n")
    readme.append(f"|[{i[:-3]}]({ref_url})|[Answer]({ans_url})|\n")

# Writing to README.md and db.txt
with open('db.txt', 'w') as f:
    f.writelines(db)
    print("db.txt updated")
with open('readme.md', 'w') as f:
    f.writelines(readme)
    print("readme.md updated")

print("New Solutions Updated")