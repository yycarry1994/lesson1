# 演示字符串切片

word = "Pizza"

print(
    """
     Slicing 'Cheat Sheet'

     0   1   2   3   4    5
     +---+---+---+---+----+
                       
     | P | i | z | z | a  |
     
     +---+---+---+---+----+
    -5  -4  -3  -2  -1

    """
    )
print("Enter the beginning and ending index for your slice of 'Pizza'.")
print("Press the enter key to exit.")

start = None
while start != "":
    start = (input("\nStart: "))

    if start:
        start = int(start)
        finish = int(input("Finish: "))

        print("word[",start,":",finish,"]is", end = "")
        print(word[start:finish])

input("\n\nPrrss thr enter key to exit.")
