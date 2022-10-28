class Parent:
    def parent_genes(self):
        print('Bidaar yo anf yaris')

class Child(Parent):
    def child_genes(self):
        print('Fanah ween')

Mohamed = Child()
print("Mohamed's Genes =")
Mohamed.child_genes()
print("///////")
print("///////")
print("Abo and Hoyo's genes given to Mohamed = ")
Mohamed.parent_genes()
