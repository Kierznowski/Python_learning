class Literowanie:
    def __init__(self, word=""):
        self.word = word
        self.maks = len(self.word)
    
    def __iter__(self):
        self.indeks = 0
        return self
        
    def __next__(self):
        if self.indeks < self.maks:
            result = self.word[self.indeks]
            self.indeks += 1
            return result
        else:
            raise StopIteration
            
literowanie = Literowanie("Hej")

for litera in literowanie:
    print(litera)
