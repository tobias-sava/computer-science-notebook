# creating task class

class Task:
    def __init__(self, description):
        self.description = description
        self.next = None # pointer to the next task (init none)
        