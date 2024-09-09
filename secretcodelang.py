'''wap  to translate a message into secret code language.
use the rules below to translate normal english into 
secret code language.

#coding
if the word contains atleast 3 characters,
remove the first letter and append it at the end.
# now append three random characters at the starting and the end
#else:
#simply reverse the string

#decoding
# if the word contains less than 3 characters,reverse it
# else:
remove 3 random characters from start and end.
now remove the last letter and append it to the beginning

your program should ask whether you want to code or decode'''

import random
import string
c=3
your_message=input("Enter your word/sentence: ")
code=input("Your message will be coded?[YES/NO]: ") 

if code=='YES':

    if len(your_message)>=3:
        a=your_message[1:]+your_message[:1]
        random_start="".join(random.choices(string.ascii_letters,k=c))
        random_end ="".join(random.choices(string.ascii_letters,k=c))
        encoded=random_start+a+random_end
    
    else:
        encoded=your_message[1:2]+your_message[:1]
    print(encoded)

else:
    print("Try Again!")
        

decode=input("Your message will be decoded?[YES/NO]: ")  
if decode=='YES':

    if len(encoded)<3:
        decoded=encoded=encoded[1:2]+encoded[:1]
        print(decoded)

    else:
        D=encoded[3:-3]
        decode= D[-1:]+D[0:-1]
        print(decode)

else:
    print("Try Again!")        






        





 