from sys import argv

print("How old are you?")
age = input()
print("How tall are you?")
tall = raw_input()
print("How much do you weigh?")
weight = raw_input()

print("So, you're %s old, %s tall and %s heavy." % (age,tall,weight))

script, filename = argv

txt = open(filename)

print("Here's your file %s:" % filename)
print(txt.read())

print("Type the filename again:")
file_again = raw_input("> ")

txt_again = open(file_again)

print(txt_again.read())


print('Let\'s practice everything.')
print("""You'd need to know \'bout escapes 
      with \ that do \n newlines and \t tabs.""")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 1
print("This should be five: %d" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars,crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print("We'd have %s beans, %s jars, and %s crates." % (beans,jars,crates))

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans,{} jars, and {} crates.".format(*formula))



people = 20
cates = 30
dogs = 15


if people < cates:
    print "Too many cats! The world is doomed!"

if people < cates:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
