temps = [221, 234, 340, 230]

new_temps = []
for temp in temps:
    new_temps.append(temp/10)

print(new_temps)

#this can be done in one line of code
#method called list comprehension

tamps = [221, 234, 340, 230]

tamps_new = [tamp / 10 for tamp in tamps]

print(tamps_new)


#list comprehension with if statement

temperature = [221, 234, 340, -9999, 230]

temp_newa = [degree / 10 for degree in temperature if degree != -9999]

print(temp_newa)

#if-selse statement

temperature = [221, 234, 340, -9999, 230]

temp_newa = [degree / 10 if degree != -9999 else 0 for degree in temperature]

print(temp_newa)

[i*2 if i>0 else 0 for i in [1, -2, 10]]