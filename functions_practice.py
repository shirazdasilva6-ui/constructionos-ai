def describe_project(project: dict) -> None:
    print(project["project_name"])
    if project["is_over_budget"]:
        print("This project needs attention!")
    else:
        print("this project is on track.")
        

project = {
    "project_name": "ConstructionOS AI",
    "active_projects": 12,
    "budget_remaining": 45000.50,
    "is_over_budget": False
}

project2 = {
    "project_name": "Stellies",
    "is_over_budget": True,
    "budget_remaining": 5000,
}

project3 = {
    "project_name": "Brakkies",
    "is_over_budget": False,
    "budget_remaining": "6500"
}

projects = [project, project2, project3]

describe_project(projects[0])
describe_project(projects[1])
describe_project(projects[2])

for project in projects:
    describe_project(project)

def is_over_budget_check(project: dict) -> bool:
    return project["is_over_budget"]

result = is_over_budget_check(project2)
print(result)

over_budget_projects = []
for project in projects:
    if is_over_budget_check(project):
        over_budget_projects.append(project)
for project in over_budget_projects:
    describe_project(project)