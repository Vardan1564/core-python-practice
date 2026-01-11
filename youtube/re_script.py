# Regular Expressions

import re

pattern=input("ENTER THE TEXT YOU WANT TO SEARCH: ")

text='''windows28 Mar 2020 — From my understanding, your aim is to connect to a server from a remote computer and send a message from the server to the client.
what SendMessage to use to send keys directly to another ...
22 Feb 2011
How can i can send Windows 10 notifications with python that ...
6 Oct 2020
Using Python to send/receive text from GUI program
2 Aug 2010
How to send a message between 2 computers - Stack Overflow
10 Aug 2020
More results from stackoverflow.com'''

# match=re.search(pattern,text)
# print(match)
match=re.finditer(pattern,text)

if match:
    for i in match:
        print(f"match the txt: {i}")
        
else:
    print("no match here")

