PLACEHOLDER = "[name]"  # Placeholder in the letter template that will be replaced by each name

# Read all names from the 'invited_names.txt' file
with open("./Input/Names/invited_names.txt", encoding='utf-8') as names_file:
    names = names_file.readlines()  # Read each line in the file, which represents a name

# Read the content of the letter template from 'starting_letter.txt'
with open("./Input/Letters/starting_letter.txt", encoding='utf-8') as letter_file:
    letter_contents = letter_file.read()  # Read the entire content of the letter template

    # Loop through each name to create a personalized letter
    for name in names:
        stripped_name = name.strip()  # Remove any leading/trailing whitespace characters from the name
        # Replace the placeholder with the current name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # Create a new file for each personalized letter in the 'ReadyToSend' folder
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", encoding='utf-8', mode="w") as completed_letter:
            completed_letter.write(new_letter)  # Write the personalized letter content to the file



