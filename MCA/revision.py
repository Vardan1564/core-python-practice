# def evenOdd(num):
#     if (num%2 == 0):
#         print("even")
#     else:
#         print("odd")

# while True:
#     con = input('Enter "yes" for Contine and "no" for Break :  ')
#     evenOdd(int(input("enter a number : ")))
#     if (con == "no"):
#         break

# def fun(a, b=2, c=3):
#     print(a, b, c)
# fun(5, c=10)


# l1 = [1,3,23,34,13,34,2,3,6,23,32]
# print(set(l1))

# l2 =[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)

# print(l2)
# print(max(l1))

# max_num = l1[0]
# for i in l1:
#     if i > max_num:
#         max_num = i

# print(max_num)


# *args is like tuple for ex. (1,2,3...100)
# def demo_args(*num):
#     total  =  0
#     for i in num:
#         print(i)
#         total += i
#     print(total)

# **kwargs is like dict for ex. {"name":"vardan" , "city":"rajkot"}
# def demo_kwargs(**kyargs):
#     for key,value in kyargs.items():
#         print(f"{key} : {value}")
    

# demo_args(1,3,4,2)
# demo_kwargs(name = 'vardan', city = 'Rajkot', phone_num=9016410956)

# def vowels(string):
#     l1 = ['a','e','i','o','u']
#     cou = 0
#     s1 = string.lower()
#     for i in s1:
#         if i in l1:
#             cou += 1
#     print(f"String -> {string} : vowels -> {cou}")

# vowels(input("Enter a String : "))

# text = "hello python..."

# print(text.endswith("python..."))

# import numpy as np

# a = np.array([1,2,3,4,2,4])
# b = np.array([2,2,4,2,4,2])

# print(a+b)

# import cv2
# import numpy as np

# # Step 1: Load an image
# image = cv2.imread('bg1.jpg')  # Loaded as a NumPy array

# # Step 2: Convert to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Step 3: Increase brightness
# brighter = np.clip(gray + 50, 0, 255)

# # Step 4: Apply a threshold filter
# _, thresholded = cv2.threshold(brighter, 128, 255, cv2.THRESH_BINARY)

# # Step 5: Display the results
# cv2.imshow("Original", image)
# cv2.imshow("Gray", gray)
# cv2.imshow("Brighter", brighter)
# cv2.imshow("Thresholded", thresholded)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# str1 = "vardan"

# print(str1[::-1])

num = int(input("enter a number : "))