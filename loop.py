for i in range(10):
    a=(i*"loosu\n")
    with open("msg.txt","a+") as f:
        f.write(a)
