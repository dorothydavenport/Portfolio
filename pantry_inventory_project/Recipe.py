# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:31:44 2024

@author: dorot
"""

"""
Dorothy Davenport
Date: 12/13/24
Class file- pantry inventory project
Description: Holds all class definitions, to be imported into main program
"""

class Recipe():
    """Creates a recipe class; a collection of ingredients and directions"""
    def __init__(self, name="", ingredients=[], directions="", servings=2):
        """Initializes the recipe class"""
        self.name = name
        self.ingredients = ingredients
        #Format of ingredients is [{Name: name, Quantity: qty, UOM: uom},
        #                          {Name: name, Quantity: qty, UOM: uom}]
        self.directions = directions
        self.servings = servings
        self.__ingredients_str = ""
        self.ingredients_list = []
    
    def add_ingredient(self, name, qty, uom):
        """Adds new ingredients to class ingredient list"""
        new_ing = {"Name":name, "Quantity":qty, "UOM":uom}
        if new_ing["UOM"] == '':
            self.__ingredients_str = f"{qty} {name}"
        else:
            self.__ingredients_str = f"{qty} {uom} {name}"
        self.ingredients.append(new_ing)
        self.ingredients_list.append(self.__ingredients_str)
        return self.ingredients
        
    def view(self):
        """Views recipe details with specific formatting"""
        print(f"RECIPE FOR: {self.name.title()}")
        print(f"Serves: {self.servings}")
        print("Ingredients:")
        for item in self.ingredients:
            if item["UOM"] == "":
                print(f"{item['Quantity']} {item['Name']}")
            else:
                print(f"{item['Quantity']} {item['UOM']} {item['Name']}")
        print("\nDirections:")
        print(f"{self.directions}\n")
        return None
    
    def scale(self, servings):
        """Scales a recipe to a certain number of servings"""
        scaled_ingredients = []
        scale_fctr = self.__scale_factor(servings)
        new_name = self.name
        new_servings = servings
        for ingredient in self.ingredients:
            scaled_ing = {}
            scaled_ing["Name"] = ingredient["Name"]
            scaled_ing["Quantity"] = round(ingredient["Quantity"] * 
                                           scale_fctr,2)
            scaled_ing["UOM"] = ingredient["UOM"]
            scaled_ingredients.append(scaled_ing)
        new_ingredients = scaled_ingredients
        new_directions = self.directions
        return Recipe(new_name, new_ingredients, new_directions, new_servings)
    
    def __scale_factor(self, servings):
        """Returns scale factor to scale a recipe"""
        if servings == self.servings:
            scale_factor = 1
        else:
            scale_factor = servings / self.servings
        return scale_factor
    
    def __str__(self):
        """Outputs the recipe string as Name- Servings, Ingredients:"""
        return f"{self.name.title()}- Serves {self.servings}, "\
               f"Ingredients: {', '.join(self.ingredients_list)}"
    
    def __contains__(self, ing):
        """Check if an ingredient is in the recipe"""
        check = False
        for dictionary in self.ingredients:
            if dictionary["Name"] == ing:
                check = True
                break
            else:
                continue
        return check

if __name__ == "__main__":
    test_recipe = Recipe()
    test_recipe.add_ingredient("pasta",1,"lb")

    assert test_recipe.ingredients == \
         [{"Name":"pasta","Quantity":1,"UOM":"lb"}], "Add ingredient failed"
    print("ASSERT TEST: Add ingredient successful!")
    print(test_recipe.ingredients)
    second_test_recipe = Recipe("Noodle dish",
                                [{"Name":"pasta","Quantity":1,"UOM":"lb"},
                                 {"Name":"sauce","Quantity":12,"UOM":"oz"}], 
                                "Make noodles and sauce",4)
    scaled_recipe = second_test_recipe.scale(2)

    assert scaled_recipe.servings == 2, "Scaled recipe failed"
    print("\nASSERT TEST: Scaled recipe successful!")
    print("Previous recipe:")
    second_test_recipe.view()
    print("Scaled recipe:")
    scaled_recipe.view()

    assert "pasta" in test_recipe, "Contains dunder failed"
    print("Contains dunder passed!")