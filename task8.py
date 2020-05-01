str1 = input('Write me any string, or sentence:\n')

print('The third character of this string:')
print(str1[2])

print('The second to last character of this string:')
print(str1[-2])

print('The first five characters of this string:')
print(str1[0:5])

print('All but the last two characters of this string:')
print(str1[0:len(str1)-2])

print('All the characters of this string with even indices:')
print(str1[0:len(str1):2])

print('All the characters of this string with odd indices:')
print(str1[1:len(str1):2])

print('All the characters of the string in reverse order:')
print(str1[-1::-1])

print('Every second character of the string in reverse order, starting from the last one:')
print(str1[-1:0:-2])

print('The length of the given string:')
print(len(str1))
