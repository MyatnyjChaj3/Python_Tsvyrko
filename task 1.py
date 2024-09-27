class Custom_b:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
    
    def __add__ (self,other):
        return self.value + str(other)
    
    def __sub__ (self,other):
        return int(self.value) - other


a = 1
b = Custom_b("31")
print(b + a)
print(b - a)