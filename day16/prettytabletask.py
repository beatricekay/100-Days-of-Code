from prettytable import PrettyTable # import PrettyTable class

# Create an object table from the PrettyTable class
table = PrettyTable()

# Add two columns with 3 rows using .add_column() method
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Change table styles by changing table object attributes
table.padding_width = 2 
print(table)

# To check the default attribute values, we print(object.attribute)
print(table.align)
