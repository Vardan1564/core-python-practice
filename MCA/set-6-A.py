seats = {
    "MP": (29, 11),
    "UP": (80, 31),
    "TN": (39, 18),
    "MH": (48, 19),
    "GJ": (26, 11),
    "RJ": (25, 10),
    "HP": (4, 3)
}

def total_s():
    total = 0
    for l,r in seats.values():
        total  += l+r    
    print(total)

total_s()

def min_r_s():
    m = []
    for i in seats.values():
        m.append(i[1])

    m_raj = min(m)
    for state,(l,r) in seats.items(): #items return key and value pare
        if m_raj == r:
            print("state : ",state)
            break

min_r_s()