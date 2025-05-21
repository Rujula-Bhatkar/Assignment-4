print("Reading file content:")
try:
    file=open("sample.txt","r")
    a=file.readline()
    print("Line 1:",a)
    b=file.readline()
    print("Line 2:",b)
    file.close()
except:
    print("Error: the file 'sample.txt' was not found.")
finally:
    print("Program Ended.")