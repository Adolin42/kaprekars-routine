# Kaprekar's Routine: https://en.wikipedia.org/wiki/Kaprekar%27s_routine
# It was discovered in 1949 by Indian recreational mathemetician D. R. Kaprekar.
# He found that if you follow a specific set of simple rules,
# every single four-digit number (with nine exceptions, where all digits are equal) eventually turns into 6174,
# otherwise known as Kaprekar's Constant.

# The Rules:
# 1) Pick a number: Choose any four digit number
#    the only rule is that the digits cannot all be the same (so 1111 or 7777 will not work)

# 2) Rearrange: Create two new numbers from your chosen digits:
#    One where the digits are in descending order
#    One where the digits are in ascending order

# 3) Subtract: Subtract the smaller number from the bigger number
#    In the event the difference ends up being fewer than 4 digits,
#    add leading zeros so the function works (92 -> 0092)

# 4) Repeat: Take your answer and repeat steps 2 and 3

def kaprekar(x: int, iterations: int):
    
    # Increment iterations
    iterations += 1
    
    # Convert to str
    s = str(x).zfill(4) # Ensures 4 digits with leading zeros

    # Create descending and ascending strings
    ascending_chars = sorted(s)
    ascending_string = ''.join(ascending_chars)

    descending_chars = sorted(s, reverse=True)
    descending_string = ''.join(descending_chars)

    # Convert strings to ints
    ascending_int = int(ascending_string)
    descending_int = int(descending_string)

     # Check for valid input (digits cannot all be the same)
    if ascending_int == descending_int:
        print("ERROR: Input cannot be four identical digits")
        return
    
    # Check for base case, input = 6174
    if x == 6174:
        print(f"Kaprekar's Constant achieved with {iterations} iterations: {x}")
        return

    # Return the difference between the bigger and smaller number
    difference = descending_int - ascending_int
    return kaprekar(difference, iterations)



def main():
    kaprekar(2886, 0)

if __name__ == "__main__":
    main()