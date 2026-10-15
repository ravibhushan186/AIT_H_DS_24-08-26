try:
    f=open("demofile.txt")
    try:
        f.write("Python is easy to learn")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opeing to the file")