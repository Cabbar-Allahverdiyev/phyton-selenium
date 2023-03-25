class Human :
    
    def __init__(self,name) :
        self.name=name;
    def __str__(self) :
        return f"Str dondu {self.name}"
h1=Human("cabb");



print(h1.name);