class Goal:
    def __init__(self, activity, quantity, metric, period):
        self.activity = activity
        self.quantity = quantity
        self.metric = metric
        self.period = period

    def __str__(self):
        return 'Goal({}, {}, {}, {})'.format(self.activity, self.quantity, self.metric, self.period)

    def __repr__(self):
        return str(self)


class Database:
    def __init__(self):
        self.goals = []

    def add_goal(self, goal: Goal):
        self.goals.append(goal)
