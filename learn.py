# Excersises

# Exercise A
completed_task = ["Wake-up", "Brush", "Bath", "Dress", "Work"]
print(completed_task[0])
print(completed_task[-1])
print(completed_task[2])

# Exercise B
shelf_stock = [5, 10, 15, 20, 30, 50]
shelf_1 = shelf_stock[0]
shelf_6 = shelf_stock[-1]
print(f"Shelf 1: {shelf_1} units")
print(f"Shelf 6: {shelf_6} units")

# Exercise C

daily_docket = [ "Adeyemi v. Briggs", 
"Estate of Okafor", 
"Chukwu & Sons Ltd v. FIRS",
"Briggs Trading Co. v. NNPC",
"Re: Emeka's Will",]
first_matter = daily_docket[0]
Third_matter = daily_docket[2]
recently_filed = daily_docket[-1]
print(first_matter)
print(Third_matter)
print(recently_filed)

# The negative indexing helps in cases where the number of items in a list is unknown and there is a requirement to produce the last item in
# the list. 
# The most recently filed would still work even if another case has been appended to it. However the index [-1] will no longer work for it 
# after the line that appends the most recent case added. 

# Exercise D

# 1. Firstly, the code becomes unnecessarily long and difficult to spot errors and different variables.
# There may be need to make calculations and putting the prices in different variables makes that difficult. 

# 2. A list makes a code easy to read and analyse# calcultions and arithmetics becomes easier. 
# 3. splitting when each number is needed may cause bugs because splitting maynot necessarity put each number into the different data values
# it was supposed to be as entries e.g floats and ints.

# Exercise E
cart_items = ["rice", "beans", "milk", "bread"]
print("First item:", cart_items[0])
print("Second item:", cart_items[1])
print("Last item:", cart_items[-1])
print("Cart:", cart_items)