number = int(input("Enter the number of students: "))
name = input("Enter the student name: ")
Tamil = float(input("Enter the tamil marks: "))
English = float(input("Enter the english marks: "))
Maths = float(input("Enter the english marks: "))
Social = float(input("Enter the social marks: "))
Science = float(input("Enter the science marks: "))
Pass=40
Total=((Tamil+English+Science+Social+Maths)/500)*100
    
if Tamil<=Pass and English<=Pass and Science<=Pass and Social<=Pass and Maths<=Pass:
            print("Candidate Failed needs reappear")
    
            if Total>90 and Total<=100:
                print(f"Candidate passed {round(Total,1)} and secured A")
            elif Total>80 and Total<=89:
                print(f"Candidate passed {round(Total,1)} and secured B")
            elif Total>70 and Total<=79:
                print(f"Candidate passed {round(Total,1)} and secured C")
            elif Total>60 and Total<=69:
                print(f"Candidate passed {round(Total,1)} and secured D")
            elif Total<60:
                print(f"Candidate failed {round(Total,1)} and needs reappear E")
else:
        print(f"Candiate failed {round(Total,1)} needs reappear F")

for i in range(1,number+1):
    Output = input("Enter the grade:")
    directory = "H:\Besant_tech\\"
  
# get fileName from user 
    filepath = directory + input("Enter filename: ") 
  
# Creates a new file 2
    with open(filepath, 'x') as fp: 
        fp = fp.write(f"{Total} \t {Output}")
