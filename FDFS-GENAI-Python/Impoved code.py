number = int(input("Enter the number of students: "))
Pass = 40

for i in range(number):
    name = input("Enter the name: ")
    with open(f"D:\\{name}.txt", "w") as f:  # Use 'w' mode to open the file for writing
        Tamil = float(input("Enter the Tamil marks: "))
        English = float(input("Enter the English marks: "))
        Maths = float(input("Enter the Maths marks: "))
        Social = float(input("Enter the Social marks: "))
        Science = float(input("Enter the Science marks: "))
        Total = ((Tamil + English + Science + Social + Maths) / 500) * 100
        f.write(f"Name: {name}\nTamil marks: {Tamil}\nEnglish marks: {English}\nScience marks: {Science}\nSocial marks: {Social}\nMaths marks: {Maths}\nTotal marks: {Total:.2f}\n")

        if Tamil >= Pass and English >= Pass and Science >= Pass and Social >= Pass and Maths >= Pass:
            if Total >= 90 and Total <= 100:
                f.write("Secured A grade\n")
            elif Total >= 80 and Total <= 89:
                f.write("Secured B grade\n")
            elif Total >= 70 and Total <= 79:
                f.write("Secured C grade\n")
                
            elif Total >= 60 and Total <= 69:
                f.write("Secured D grade\n")
            else:
                f.write("Secured E grade\n")
        else:
            print(f"Candidate {name} failed with {round(Total, 1)}%")
            f.write("Secured F grade and Failed\n")

    name = input("Enter the name: ")
    directory = "H:\Besant_tech\\"
  # get fileName from user 
    filepath = directory + name

  # Creates a new file
with open(filepath, 'x') as fp:
    fp = fp.write(f"Name: {name} \t {Total} \t {Output} \n Tamil: {Tamil} \n English: {English} \n Science: {Science} \n Social: {Social} \n Maths: {Maths}")