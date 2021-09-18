name_is_above_3 =  False
name_is_below_50 = True

if name_is_above_3 and not name_is_below_50:
    print("Name can only be a maximum of 50 characters")

elif name_is_below_50 and not name_is_above_3:
    print("Name must me at leat 3 characthers long")

elif name_is_above_3 and name_is_below_50:
    print("Name looks good!!!")
