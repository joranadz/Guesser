print("""
I will gues your number, you have to think the number bitven 1 and 500. 
And I will gess it!
If I say to big please write '<' and if to smal write '>'""")
print("When you will be raedy write 'play'")
number = int(250)
while True:
    new_number_smal=int(number/2)
    new_number_big=int(number/2+251)
    gess = input()
    if gess =="play":
        print("is it 250?")
    elif gess =="<":
        print(new_number_smal)
        number=new_number_smal
    elif gess ==">":
        print(new_number_big)
        number=new_number_big
    elif gess =="yes":
        print("I win and your number is")
        print(number)
        break
    else:
        print("Please repet answer?")
        break
