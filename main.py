import random

rand_num= random.randint(1000, 9999)
print(rand_num)


def function():
    user_in = input("Enter your number: ")
    print(user_in)

    rcount = 0
    tcount = 0
    srand_num = str(rand_num)

    if len(user_in) != 4:
        print("invalid")
    else:
        if user_in == srand_num:
            print("WINNER")
            yes_or_no_check()

        else:
            for x in range(0,4):
                for y in range(0,4):
                    if x == y:
                        if srand_num[x]==user_in[y]:
                            rcount =rcount+1
                            continue
                    elif srand_num[y]==user_in[x] :
                           tcount=tcount+1

        print("you got rabbit", rcount)
        print("you got tortoise", tcount)
    yes_or_no_check()


def yes_or_no_check():
    b = input("Do You Want To Continue? [y/n]")
    if b == 'n' or b == 'N':
        exit(0)
    elif b == 'y' or b == 'Y':
        function()


function()
if __name__ == '__function__':
    function()
