number = int(input("Enter the number of students: "))
Pass=40

for i in range(number):
    name = input("Enter the name: ")
    directory = "H:\Besant_tech\\"
    filepath = directory + name
    with open(f"{filepath}","x") as f:
        Tamil = float(input("Enter the tamil marks: "))
        English = float(input("Enter the english marks: "))
        Maths = float(input("Enter the english marks: "))
        Social = float(input("Enter the social marks: "))
        Science = float(input("Enter the science marks: "))
        Total=Tamil+English+Science+Social+Maths
        Per=(Total/500)*100
        print(f"Total marks: {Total}, Percentage:{Per}")
        f.write(f"{name} \n Tamil marks: {Tamil} \n English marks: {English} \n Science marks: {Science} \n Social marks: {Social} \n Maths marks: {Maths} \n Total marks: {Total} \n Total percentage: {round(Per,1)}")

        
        if Tamil>=Pass and English>=Pass and Science>=Pass and Social>=Pass and Maths>=Pass:
            if Per>=90 and Per<=100:
                f.write(f"\n Secured A grade")
            elif Per>=80 and Per<=89:
                f.write(f" \n Secured B grade")
            elif Per>=70 and Per<=79:
                f.write(f" \n Secured C grade")
            elif Per>=60 and Per<=69:
                f.write(f" \n Secured D grade")
            else:
                f.write(f" \n Secured E grade")

        else:
            print(f"Candiate failed {round(Per,1)}")
            f.write(f" \n Secured F grade and Failed")
            
        

       
