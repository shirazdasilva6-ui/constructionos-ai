class Project:
    def __init__(self, name: str, budget_remaining: float, is_over_budget: bool):
        self.name = name
        self.budget_remaining = budget_remaining
        self.is_over_budget = is_over_budget

    def describe(self) -> None:
        print(self.name)
        if self.is_over_budget:
            print("this project needs attention")
        else:
            print("this project is on track")


stellies = Project("stellies", 5000, True)
stellies.describe()
print(stellies.budget_remaining)

ConstructionOS_AI = Project("ConstructionOS_AI", 4500.50, False)
ConstructionOS_AI.describe()
print(ConstructionOS_AI.budget_remaining)

Brakkies = Project("brakkies", 6500, False)
Brakkies.describe()
print(Brakkies.budget_remaining)




