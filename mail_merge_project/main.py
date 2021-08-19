#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("mail_merge_project/input/names/invited_names.txt") as file:
    name_list = []
    for name in file.readlines():
        format_name = name.strip("\n")
        name_list.append(format_name)

with open("mail_merge_project/input/letters/starting_letter.txt") as starting_letter:
    contents = starting_letter.read()

for name in name_list:
    new_contents = contents.replace("[name]", name)
    with open(f"mail_merge_project/output/readytosend/letter_for_{name}.txt", mode="w") as file:
        file.write(new_contents)