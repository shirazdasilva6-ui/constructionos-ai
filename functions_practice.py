def describe_project(project):
    print(project["project_name"])
    print(project["is_over_budget"])

project = {
    "project_name": "ConstructionOS AI",
    "active_projects": 12,
    "budget_remaining": 45000.50,
    "is_over_budget": False
}
describe_project(project)    
