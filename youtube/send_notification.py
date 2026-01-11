# simple way to make windows notification like normal pop-up notification 
from win10toast import ToastNotifier

# here make variable of ToastNotifier() this method
toaster= ToastNotifier()

#first is title of notification and next is messege 
toaster.show_toast("hiii","hello world",duration=5)

# way 2 ---------------------

from winotify import Notification,audio

t=Notification(app_id="WATER REMINDER",
               title="drink water",
               msg="pani pile loda have tuuu",
               duration="long",
               icon="D:/PROJECT/Images/favicon.ico")

t.set_audio(audio.Reminder,loop=True)

t.show()

# t=Notification(
#     app_id="abc",
#     title="water",
#     msg="hello how are you",
#     duration="long"
# )
# t.set_audio(audio.LoopingCall7,loop=True)

# t.show()