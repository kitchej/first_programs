class Human:
    def __init__(self, name, gender, height, weight):
        """the __init__(self) method is called a "constructor." This method is what builds (or constructs) objects.
        The "self" argument is passed in as the name of the object and allows for easier calling of methods and class
         attributes"""
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight

    def get_bmi(self):
        bmi = 703*(self.weight/(self.height*self.height))
        return round(bmi, 2)

    def show_attributes(self):
        print(self.name)
        print(self.gender)
        print(str(self.height) + " inches")
        print(str(self.weight) + " pounds")


class SuperHuman(Human):
    def __init__(self, name, gender, height, weight, super_power, is_a_villain):
        super().__init__(name, gender, height, weight)
        # super().__init__ allows inheritance of both class constructors AND methods
        # ParentClassName.___init___ will only allow inheritance of class constructors
        self.super_power = super_power
        self.is_a_villain = is_a_villain

    def show_attributes(self):
        # defining a method with the same name in the child class will override
        # the method inherited from the parent class
        print(self.name)
        print(self.gender)
        print("Height: " + str(self.height) + " inches")
        print("Weight: " + str(self.weight) + " pounds")
        print("Powers: ")
        for powers in self.super_power:
            print(powers)
        if self.is_a_villain:
            print("Status: Villain")
        else:
            print("Status: Hero")


human1 = Human("Greg", "Male", 73, 180)
wonder_woman = SuperHuman("Diana", "Female", 69, 150, ["Strength", "Agility", "Immortality"], False)

greg_bmi = human1.get_bmi()

print(f"{human1.name}'s bmi is {greg_bmi}\n")

wonder_woman.show_attributes()

num_str = "70"

reg_num = 70

print(int(num_str) - 2)

