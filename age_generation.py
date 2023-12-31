# No Name       2013 - ?
# Gen Z	        1997 – 2012
# Millennials	1981 – 1996
# Gen X	        1965 – 1980
# Boomers II*	1955 – 1964
# Boomers I*	1946 – 1954
# No Name	    ?  - 1945

# Write a function to return generation name of the given year of birth

def get_generation_name(year_of_birth):

    if year_of_birth <= 1945:
        return "No Name"

    if year_of_birth <= 1954:
        return "Boomers I"

    if year_of_birth <= 1964:
        return "Boomers II"

    if year_of_birth <= 1980:
        return "Gen X"

    if year_of_birth <= 1996:
        return "Millennials"

    if year_of_birth <= 2012:
        return "Gen Z"

    return "No Name"

##### CALL function ##########

yob = 1981
gen_name = get_generation_name(yob)

print(f"Generation name of YoB {yob} is {gen_name}")