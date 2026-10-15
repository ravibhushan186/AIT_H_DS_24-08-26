import csv

# -----------'r' read --------------
# with open('data.csv', 'r') as f:
#     res = csv.reader(f)
#     # print(res)
#     # print(list(res))

#     info = list(res)
#     print(info[0][0], info[0][1], info[0][2])


# ----------'w' write ---------------------
# data = [
#     ['stu_id', 'Name', 'age'],
#     [101, 'Ravi', 23],
#     [102, 'Bhushan', 24],
#     [103, 'Pankaj', 25]
# ]

# with open('stu.csv', 'w', newline="") as f: # iused newline="" why because to remove the space from the data
#     writer = csv.writer(f)
#     writer.writerows(data)


# --------- DictReader-------------
# with open('data.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for i  in reader:
#         # print(i)
#         print(i['id'], i['name'],i['email'])


# ----- 'w' write----------

# data1 = [
#     {'id':101, 'Name':'Ravi', 'age':21},
#     {'id':102, 'Name':'Bhushan', 'age':23},
#     {'id':103, 'Name':'Aman', 'age':22}
# ]

# with open('stu1.csv', 'w', newline="") as f:
#     fielsnames = ['id', 'Name', 'age']
#     w = csv.DictWriter(f, fieldnames=fielsnames)
#     w.writeheader()
#     w.writerows(data1)