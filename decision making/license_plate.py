def old_new_license():
    platenum = input()
    length = len(platenum)
    if length == 6:
        if platenum[0].isupper() and  platenum[1].isupper() and platenum[2].isupper() and platenum[3].isdigit() and platenum[4].isdigit() and platenum[5].isdigit():
            print("OLD version of license plate")
        else:
            print("Not valid version")
    elif length == 7:
        if platenum[0].isdigit() and  platenum[1].isdigit() and platenum[2].isdigit() and platenum[3].isdigit() and platenum[4].isupper() and platenum[5].isupper() and platenum[6].isupper():

            print("New version of license plate")
        else:
            print("Not valid version")
    else:
        print("Not valid version")
old_new_license()