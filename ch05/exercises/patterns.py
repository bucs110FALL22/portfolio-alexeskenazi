def star_pyramid(): 
  rows = int(input("Type the # of Rows : ")) 
  for i in range(rows): 
    for j in range(i+1):
      print("* ", end="")
    print("\n")
 