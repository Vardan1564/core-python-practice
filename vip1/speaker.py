import win32com.client 

l=["rahul","vardan","shree"]

bol= win32com.client.Dispatch("Excel.Application")

bol.speak(l)

