#step 1 : writing marks to marks1.txt
marks = open("marks1.txt","w")
student_name = input("Enter Student Name : ")
english_marks = int(input("Enter Marks obtained in English : "))
hindi_marks = int(input("Enter Marks obtained in Hindi : "))
maths_marks = int(input("Enter Marks obtained in Maths : "))
details = "{},{},{},{}".format(student_name,english_marks,hindi_marks,maths_marks)
marks.write(details)
marks.close()

#Step 2 : reading marks from marks1.txt and calculating average and total marks  
data_file = open("marks1.txt","r")
data = data_file.read()
#print(data)
record = data.split(",")
#print(record)
total = 0 
for i in range(1,len(record)):
    total = total + int(record[i])
average = total/(len(record)-1)
#print(total,average)
data_file.close()

#step 3 : writing data in results.txt 
file = open("results.txt","w")
record.append(str(total))
record.append(str(average))
#print(record)
details = record[0]
for i in range(1,len(record)) : 
    details = details + "," + record[i]
#print(details)
file.write(details)
file.close()


#step 4: read result data and display to the user
file=open("results.txt","r")
data=file.read()
record=data.split(",")
print("==========================")
print("welcome to our portal")
print("==========================")
print("herer is your result")
print("student name:",record[0])
print("marks in english:{} out of {}".format(record[1],20))
print("marks in hindi:{} out of {}".format(record[2],20))
print("marks in maths:{} out of {}".format(record[3],20))
print("total marks:{} out of {}".format(record[4],60))
print("average marks:",record[5])
print("==========================")
file.close
print

