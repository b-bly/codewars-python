def six_column_encryption(msg):
    msg_list = []
    msg_lists = []
    spaces = 0

    # replace spaces with "."
    msg = msg.replace(" ", ".")

    # add enough "." if the last row (of 6) is not completely full.
    if (len(msg) % 6):
        spaces = 6-(len(msg) % 6)
    msg += "." * spaces

    # make a list of lists of characters, 6 char long.
    for j in range(0, len(msg)):
        msg_list.append(msg[j])
        if not (j + 1) % 6:
            msg_lists.append(msg_list)
            msg_list = []
        if j == len(msg) -1: print(msg_list)
  
    #add a row of spaces
    msg_lists.append([" "]*6)
    output = ""

    # append the nth letter in each row to a growing string
    for i in range(0, 6):
        for j in range(0, len(msg_lists)):
            output += msg_lists[j][i]

    #remove the final space
    output = output[:-1]
    print(output)

attack = "Attack at noon or we are done for"
nonsense = "nvxlkut ehed kmdg idbemb qm hicihdp ylkbl enm oulvo yw znqqj"



msg = 'abcdefghijklmnopq'
a = [msg[n::6] for n in range(6)]
print(a)
