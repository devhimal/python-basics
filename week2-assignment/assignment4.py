ceos = ["Alice Johnson", "Bob Smith", "Charlie Brown", "Diana Prince", "Eve Adams"]
name_dict = {}

for full_name in ceos:
    first_name, last_name = full_name.split()
    if last_name not in name_dict:
        name_dict[last_name] =[] 
    name_dict[last_name].append(first_name)

print("CEO Names Dictionary:", name_dict)
