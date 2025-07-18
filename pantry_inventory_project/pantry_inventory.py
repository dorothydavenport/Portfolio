# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 15:25:52 2024

@author: dorot
"""

"""
Dorothy Davenport
Date: 12/13/24
Description: Allows user to maintain an ingredient inventory and recipe 
collection
"""

import csv
from Recipe import Recipe

def establish_inventory():
    """Loads all item names from the inventory file to the program as a set"""
    inv_set = set()
    try:
        with open("pantry_inventory.csv", "r", encoding="utf-8-sig") as infile:
            csv_file = csv.DictReader(infile, fieldnames=("item_name",
                                                          "quantity",
                                                          "size",
                                                          "uom", 
                                                          "cost"))
            for row in csv_file:
                inv_set.add(row["item_name"])
    except (FileNotFoundError()):
        print("File not found.")
    return inv_set

def add_ingredient():
    """Adds a single ingredient to inventory"""
    item_name = input("Enter the item name to add: ")
    if item_name not in full_ingredient_set:
        item_qty = float(input("Enter the item quantity to add as a number "
                         "or decimal: "))
        item_size = float(input("Enter the size of the item as a number "
                          "(if 24oz, enter 24): "))
        item_uom = ingredient_uom()
        item_cost = float(input("Enter the price paid per uom: "))
        new_item = {"Item Name":item_name,
                    "Quantity":item_qty, 
                    "Size": item_size, 
                    "UOM": item_uom, 
                    "Cost":item_cost}
        full_ingredient_set.add(new_item["Item Name"])
        return new_item
    else:
        print("That item is already in your inventory")
        return None

def view_ingredient(ing_dict):
    """Displays a single ingredient's details"""
    for idx,val in ing_dict.items():
        print(f"{idx}: {val}")
    return None

def write_ingredient(name, qty, size, uom, cost):
    """Writes ingredient details to a csv file"""
    try:
        with open("pantry_inventory.csv", "a+", encoding="utf-8-sig", 
                  newline='') as inventory_file:
            fieldnames = ["item_name","quantity","size","uom", "cost"]
            csv_write_file = csv.DictWriter(inventory_file, 
                                            fieldnames=fieldnames, 
                                            lineterminator = '\n')
            csv_write_file.writerow({"item_name": name, 
                                     "quantity": qty, 
                                     "size": size, 
                                     "uom": uom, 
                                     "cost":cost})
    except FileNotFoundError:
        print("File not found.")
    else:
        print("\n**Ingredient Added**\n")
    return None

def view_inventory():
    """Displays all items in inventory"""
    try:
        with open("pantry_inventory.csv", "r", encoding="utf-8-sig") as infile:
            csv_file = csv.DictReader(infile, fieldnames=("item_name",
                                                          "quantity",
                                                          "size",
                                                          "uom", 
                                                          "cost"))
            for row in csv_file:
                print(f"{row['item_name']:<15} {row['quantity']:<8} "\
                      f"{row['size']:<4} {row['uom']:<8} {row['cost']:<4}")
                full_ingredient_set.add(row["item_name"])
    except (FileNotFoundError()):
        print("File not found.")
    return None

def find_recipe(search_name):
    """Finds a recipe in the recipe catalog"""
    check = False
    returned_recipe = Recipe()
    for recipe in full_recipe_catalog:
        if search_name.lower() == recipe.name.lower():
            check = True
            returned_recipe = recipe
            break
        else:
            continue
    return check, returned_recipe

def print_menu():
    """Displays the main program menu"""
    print("\nMain Menu:\n"
          "1. Add an ingredient\n"
          "2. View pantry inventory\n"
          "3. Create a recipe\n"
          "4. View recipe catalog\n"
          "5. Scale a recipe\n"
          "6. Exit program")
    return None

def ingredient_uom():
    """Displays the menu for selecting an ingredient uom"""
    ingredient_uomtupe = ("teaspoon", "tablespoon", "cup", "lb",
                        "oz", "fl oz", "gram", "None")
    print_again = True
    while print_again == True:
        print("\nIngredient uom options:\n"
              "1. teaspoon\n"
              "2. tablespoon\n"
              "3. cup\n"
              "4. lb\n"
              "5. oz\n"
              "6. fl oz\n"
              "7. gram\n"
              "8. None (use for items like whole vegetables, ex 1 pepper)")
        selection = input("Select the menu number for the ingredient's "\
                              "unit of measurement: ")
        if selection.isalpha() == True or int(selection) not in \
                                            range(1,len(ingredient_uomtupe)+1):
            print("That is not an option, please select again.\n") 
        else:
            selection = int(selection)
            print_again = False
    uom = ingredient_uomtupe[selection - 1]
    return uom

#MAIN PROGRAM
if __name__ == '__main__':
    print("\n*** Pantry organization and recipe creation tool ***")
    full_ingredient_set = establish_inventory()
    full_recipe_catalog = []
    reprompt = True
    while reprompt == True:
        print_menu()
        selection = input("Select an option: ")
        if selection == "1": 
            #Adds an ingredient and saves it to the inventory file
            add_another = True
            while add_another == True:
                new_ingredient = add_ingredient()
                if new_ingredient is not None:
                    write_ingredient(
                        new_ingredient["Item Name"], 
                        new_ingredient["Quantity"], 
                        new_ingredient["Size"], 
                        new_ingredient["UOM"], 
                        new_ingredient["Cost"])
                    print("You entered the following: ")
                    view_ingredient(new_ingredient)
                    another = str()
                    while another.lower() != "yes" and another.lower() != "no":
                        another = input("\nDo you want to add another item? "
                                        "(Yes/No): ")
                        if another.lower() == "yes":
                            add_another = True
                        elif another.lower() == "no":
                            add_another = False
                        else:
                            print("You may only enter Yes or No")
                else:
                    add_another = False
            reprompt = True
        elif selection == "2": 
            #Opens inventory file and reads each line
            print("\nHere is a look at your current inventory contents:\n")
            view_inventory()
            reprompt = True
        elif selection == "3":
            #Creates a new recipe and then displays it
            new_recipe = Recipe()
            new_recipe.name = input("What is the name of your recipe?: ")
            recipe_exists = find_recipe(new_recipe.name)
            if recipe_exists[0] == False:
                enter_again = True
                while enter_again == True:
                    try:
                        new_recipe.servings = int(input("How many does it "
                                                        "serve?: "))
                    except ValueError:
                        print("Please only enter a number.")
                    else:
                        enter_again = False
                another_ing = True
                while another_ing == True:
                    ing_name = input("Enter the ingredient name: ")
                    ing_qty = float(input("Enter the ingredient quantity " 
                                    "(ex. if 1 tablespoon enter 1): "))
                    ing_uom = ingredient_uom()
                    if ing_uom == "None":
                        ing_uom = ""
                    new_recipe.ingredients = new_recipe.add_ingredient(
                        ing_name, 
                        ing_qty, 
                        ing_uom)
                    enter_another = input("Enter another ingredient? (Y/N): ")
                    if enter_another.upper() == "Y":
                        another_ing = True
                    else:
                        another_ing = False
                new_recipe.directions = input("Enter the recipe directions: ")
                print("Your recipe is below:\n")
                new_recipe.view()
                full_recipe_catalog.append(new_recipe)
            else:
                print("That recipe is already in your catalog.")
            reprompt = True
        elif selection == "4":
            print("\nHere is a look at your current recipe catalog:\n")
            if len(full_recipe_catalog) == 0:
                print("No recipes added.")
            else:
                for recipe in full_recipe_catalog:
                    print(recipe)
            reprompt = True
        elif selection == "5":
            if len(full_recipe_catalog) == 0:
                print("\nNo recipes available to scale.")
            else:
                recipe_choice = input("\nEnter the name of the recipe you'd "\
                                      "like to scale: ")
                recipe_exists = find_recipe(recipe_choice)
                if recipe_exists[0] != False:
                    recipe_to_scale = recipe_exists[1]
                    print("Current recipe version: ")
                    recipe_to_scale.view()
                    new_servings = int(input("Enter the new number of servings"
                                             " as an integer: "))
                    print("Scaled recipe version: ")
                    scaled_recipe = recipe_to_scale.scale(new_servings)
                    scaled_recipe.view()
                else:
                    print("That recipe is not in your catalog.")
                    reprompt = True
        elif selection == "6":
            print("Program closed")
            reprompt = False
        else:
            print("That is not an option, please select again.\n")
