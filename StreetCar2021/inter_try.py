from Traffic_lights import Street

street = Street(0,1,"rue de paris", 4)

print(str(street) + " ",
str(street.start) + " ",
str(street.end) + " ",
str(street.name) + " ",
str(street.length))

apple = street

print(str(apple) + " ",
str(apple.start) + " ",
str(apple.end) + " ",
str(apple.name) + " ",
str(apple.length))

print(str(street) + " ",
str(street.start) + " ",
str(street.end) + " ",
str(street.name) + " ",
str(street.length))
