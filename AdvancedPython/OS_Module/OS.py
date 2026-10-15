import os

#1). To know current workin directory?

# cwd = os.getcwd()
# print("Current working directory: ", cwd)

# 2).To create a sub directory in cwd?

# os.mkdir('DataScience')
# print('Task Completed')

#3). To create a sub directory in DataScience

# os.mkdir('DataScience/DeepLearning')
# print("Task Completed")

# 4). To create multiple directories like dir1 in that dir2 in that dir3..

# os.makedirs('DS/advpython/fileio')
# print('Task Completed')

# 5). To remove a directory (it will remove DeepLearning only)

# os.rmdir('DataScience/DeepLearning')
# print('Task Completed')

#6). To remove a directory multiple folder at once(It will remove all the and folders)

# os.removedirs('DS/advpython/fileio')
# print('Task Completed')

# 7). TO rename a directory
# os.rename('DataScience','DS')
# print('Task Completed')

# 8). To know contents of directory:
# print(os.listdir('DS'))


# 9). To know contents of directory including sub directories:

# for dirpath,dirname,filename in os.walk('.'): # Here . represent the current directory
#     print('Current Directory path: ', dirpath)
#     print('Directories: ', dirname)
#     print('Files: ',filename)


# 10). How to run other program from python progra
# dir *.py  

# print('OS.py executing.. and it list out all python files present in cwd')
# os.system('dir *.py')

# 10).I want to open notepad with the help of code

# print('Opening notepad while executing..')
# os.system('notepad')

# 11). I am going to execute the another Demo.py to run using OS.py

# print('Executing.. Demo.py ')
# os.system('python Demo.py')

# 12). How to open calculator using code

# print('Opening Calculator...')
# os.system('calc')