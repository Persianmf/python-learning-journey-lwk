import math
print("hi gng")
while True:
  choice = input("A = AREA\nB = BASIC STUFF\n: ").upper()
  if choice == "A":
    print("AREA OF:\nC = CIRCLE\nT = TRIANGLE\nR = RECTANGLE\nP = PARALELLOGRAM\nTR = TRAPEZOID")
    area = input("choose one gng: ").upper()
    if area == "C":
      radius = input("RADIUS: ")
      print((int(radius) ** 2) * math.pi)
    if area == "T":
      base = input("BASE: ")
      height = input("HEIGHT: ")
      print((int(base) * int(height)) / 2)
    if area == "R":
      length = input("LENGTH: ")
      width = input("WIDTH: ")
      print((int(length) * int(width)))
    if area == "P":
      base1 = input("BASE: ")
      height1 = input("HEIGHT: ")
      print((int(base1) * int(height1)))
    if area == "TR":
      num1 = input("length: ")
      num2 = input("other length: ")
      height2 = input("height: ")
      print(((int(num1) + int(num2)) * int(height2) / 2))
  if choice == "B":
    print("+ = PLUS\n- = MINUS\nx = TIMES\n/ = DIVIDE")
    num1 = input("ENTER A NUMBER >>> ")
    num2 = input("ENTER A 2ND NUMBER >>> ")
    fnc = input("ENTER A FUNCTION >>> ")
    if fnc == "+":
      print(int(num1) + int(num2))
    elif fnc == "-":
      print(int(num1) - int(num2))
    elif fnc == "x":
      print(int(num1) * int(num2))
    elif fnc == "/":
      print(int(num1) / int(num2))
  des = input("ANOTHER?(Y/N):").upper()

  if des == "N":
      print("Goodbye!")
      break