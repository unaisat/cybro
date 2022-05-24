import random
rand = random.randint(1000, 9999)
print(rand)


def function():
    user_input = input("enter your number :")
    print(user_input)


    string_rand = str(rand)
    string_user_input = str(user_input)

    count=0
    tcount = 0

    if string_rand == string_user_input:
        print("winner")
    else:
        for i in string_rand:
            for j in string_user_input:
                if i == j:
                    if str(string_rand.index(i)) == str(string_user_input.index(j)):
                        print("Same at %dth position" % (string_rand.index(j)))
                        print("you got rabbit")
                        count = count+1;
                        break
                    else:
                        print("tortoise")
                        tcount = tcount+1;
        print("rabit count", count)
        print("tortoise count", tcount)
    yes_or_no_check()



def yes_or_no_check():
    b = input("Do You Want To Continue?")
    if b == 'n' or b == 'N':
        exit(0)
    elif b == 'y' or b == 'Y':
        function()

function()
if __name__ == '__function__':
    function()




