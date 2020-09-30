#string operations are performed

#def word_with_longest_length():
#def Words(str):
h is :", len(longest_wordlist = []
temp = ""
for i in str:
    if i == ' ':
        list.append(temp)
        temp = ""
    else:
        temp = temp + i
list.append(temp)
return list
str = input("Enter the String : ")
    list = Words(str)
    longest_word = list[0]
    for i in list:
        if len(i) > len(longest_word):
            longest_word = i
    print("Longest word is :", longest_word, "\nAnd its lengt))


def frequency_of_occurrence_of_character():
    str = input("Enter the string : ")
    newstr = list(str)
    list1 = []
    for j in newstr:
        if j not in list1:
            list1.append(j)
            count = 0
            for i in range(len(newstr)):
                if j == newstr[i]:
                    count += 1
            print("{} - {} times".format(j, count))



def palindrome_check():
    str = input("Enter string : ")
    if (str == str[::-1]):
        print("The string is palindrome")
    else:
        print("The string isn't palindrome")



def index_of_appearance_of_the_substring():
    string = input("Enter the string : ")
    sub_string = input("Enter the sub_string : ")
    print("string : ", string, "\nsub_string :", sub_string)
    res = []
    flag = 0
    k = 0
    for i in range(0, len(string)):
        k = i
        flag = 0
        for j in range(0, len(sub_string)):
            if string[k] != sub_string[j]:
                flag = 1
            if flag:
                break
            k = k + 1
        if flag == 0:
            res.append(i)
    print("resultant positions", str(res))



def occurrences_of_each_word_in_a_string():
    string = input("Enter string : ")
    string = string.lower()
    words = []
    words_count = {}
    temp = ''
    for char in string:
        if char == ' ':
            words.append(temp)
            temp = ''
        else:
            temp = temp + char
    words.append(temp)
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    for word, count in words_count.items():
        print(word, count)



while(1):
    print("""\n1.Word with the longest length \n2.Frequency of occurrence of character \n3.String is palindrome or not \n4.Index of first appearance of the substring \n5.Occurrences of each word in a string""")
    print("-1 to exit")
    z=int(input("\nEnter your choice : "))
    if (z==-1):
          print("You are exited")
          break
    elif(z==1):
        Words(str)
    elif(z==2):
        frequency_of_occurrence_of_character()
    elif(z==3):
        palindrome_check()
    elif(z==4):
        index_of_appearance_of_the_substring()
    elif(z==5):
        occurrences_of_each_word_in_a_string()
    else:
        print("Wrong choice")
        break








