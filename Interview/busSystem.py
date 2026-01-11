seat = 40
booking = [1,3]
num = 1
for i in range(10):
    print(num, num+1,"  ",num+2, num+3)
    num += 4

print("_"*20,"\n")

numBookingSeat = int(input("Enter a Total Number Seat You Want to Book : "))

print("_"*40,"\n")

# seatNumberOnce = []
# for seats in range(numBookingSeat):
#     seatNumber = int(input("Enter a Seat Number For Booking Seat : "))
    
#     if seatNumber in booking or seatNumber <= 0 or seatNumber > 40:
#         print("This seat is not Available..😔 Sorry..🙏 Please Select Other Once.. 😊")
#         numBookingSeat += 1
#     else:
#         booking.append(seatNumber)
#         seatNumberOnce.append(seatNumber)

new_booking = []

while len(new_booking) < seat:
    seatNumbers = int(input("Enter a Seat Number For Booking Seat : "))

    if seatNumbers < 1 or seatNumbers > 40:
        print("❌ Invalid seat number. Please choose between 1 and 40.")
    elif seatNumbers in booking or seatNumbers in new_booking:
        print("❌ Seat not available. Please choose another.")
    else:
        booking.append(seatNumbers)
        new_booking.append(seatNumbers)
        print("✅ Seat booked successfully!")


print("_"*40,"\n")

print("Your Booking Seats : ",seatNumbers)


