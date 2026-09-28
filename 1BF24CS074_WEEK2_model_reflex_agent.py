class VacuumCleaner:
    def __init__(self):
        self.model = {
            "A": "Unknown",
            "B": "Unknown"
        }
        self.location = "A"
    def perceive(self, environment):
        return environment[self.location]
    def update_model(self, percept):
        self.model[self.location] = percept
    def choose_action(self, percept):
        if percept == "Dirty":
            return "Suck"
        elif self.location == "A":
            return "Move Right"
        else:
            return "Move Left"
    def act(self, action, environment):
        if action == "Suck":
            environment[self.location] = "Clean"
        elif action == "Move Right":
            self.location = "B"
        elif action == "Move Left":
            self.location = "A"
    def run(self, environment, steps):
        for i in range(steps):
            print("\nStep", i + 1)
            print("Location:", self.location)
            percept = self.perceive(environment)
            print("Percept:", percept)
            self.update_model(percept)
            print("Internal Model:", self.model)
            action = self.choose_action(percept)
            print("Action:", action)
            self.act(action, environment)
            print("Environment:", environment)
environment = {
    "A": "Dirty",
    "B": "Dirty"
}
agent = VacuumCleaner()
agent.run(environment, 6)