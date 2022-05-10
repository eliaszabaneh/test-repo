
notoall = 0
yestoall = 0

print("notoall is {0} and yestoall is {1} ".format(notoall, yestoall))
for index in range(0,50):
    print("message number {0}".format(index))
    if (notoall == 0) and (yestoall == 0):
        print("notoall is {0} and yestoall is {1} and index is {2}".format(notoall,yestoall,index))
        answer = input("do you want to delete all none or just this message?(none/all/this): ")
        if answer == "none":
            print("The answer is \"none\"")
            notoall = 1
            pass
        elif answer == "all":
            print("The answer is \"all\"")
            yestoall = 1
            pass
        else:
            print("The answer is \"this\"")
            print("deleting message ({0})".format(index))
            continue
    if notoall == 1:
        print("not deleting message({0})".format(index))
    elif yestoall == 1:
        print("deleting message({0})".format(index))

# print("message number {0}".format(index))

# if na == True:
#     continue
#
#     if input("Delete the message {0} received from {1}? (y/n): ".format(message_id, messageFrom)) == 'y':
#         deleteMessage(message_id, service, cur, con)
#         print("Message {0} deleted".format(message_id))