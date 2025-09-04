#old Version
# Finding Cats and Mouse
# Author: A.G. Hasan Zarook
def place_of_CatA_CatB_Mouse_Respectively(a,b,c):
   
    if (c-a) < (b-c):
        return 'Cat A'
    elif (c-a) > (b-c):
        return 'Cat B'
    else:
        return 'Mouse C'
var=0
while var==0:
    x=int(input("Enter the place of Cat A: "))
    y=int(input("Enter the place of Cat B: "))
    z=int(input("Enter the place of Mouse C: "))      
    k=place_of_CatA_CatB_Mouse_Respectively(x,y,z)
    print("Expecting Animal is: ",k,)
    print("/n")


#Updated Version
# Finding Cats and Mouse
# Author: A.G. Hasan Zarook

def place_of_CatA_CatB_Mouse_Respectively(a, b, c):
    """Return which cat will catch the mouse, or if the mouse escapes."""
    dist_a = abs(c - a)
    dist_b = abs(c - b)

    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    else:
        return "Mouse C"

def main():
    while True:
        try:
            x = int(input("Enter the place of Cat A: "))
            y = int(input("Enter the place of Cat B: "))
            z = int(input("Enter the place of Mouse C: "))
            
            result = place_of_CatA_CatB_Mouse_Respectively(x, y, z)
            print("Expecting Animal is:", result, "\n")

            # Ask user if they want to continue
            again = input("Do you want to try again? (y/n): ").strip().lower()
            if again != 'y':
                print("Exiting program. Goodbye!")
                break
        except ValueError:
            print(" Invalid input! Please enter integers only.\n")

if __name__ == "__main__":
    main()
