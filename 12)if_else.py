a = int(input("Enter your age:"))
print("your age is:", a)

# condition op
# # >,<,>=,<=.!=
# print(a > 18)
# print(a < 18)
# print(a >= 18)
# print(a >= 18)
# print(a != 18)
# if
if (a > 18):
  print("you can drive")
else:
  print("you cannot driave")

# # if_else
# apple=10
# budget=500
# if(apple<=budget):
#   print("add 1 kg apples to cart")
# else:
#   print("do not add apples to cart")

apple = 10
budget = 500
if (budget - apple > 50):
  print("add 1 kg apples to cart")
elif (budget - apple > 70):
  print("its okay buy ")
