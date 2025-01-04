ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# list
ft_list[1] = "World"

# tuple
t = list(ft_tuple)
t[1] = "Morocco"
ft_tuple = tuple(t)

# set
ft_set.remove("tutu!")
ft_set.add("Benguerir")

# dict
ft_dict["Hello"] = "Benguerir Campus"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
