# Mail Merge Project

## Overview

This project performs a mail merge operation by generating personalized letters for a list of names. The script reads a list of names from a file and replaces a placeholder in a letter template with each name, creating a personalized letter for each recipient. The final letters are saved in a specified output directory.

## File Structure

- `Input/Names/invited_names.txt`: A text file containing the list of names, each on a new line.
- `Input/Letters/starting_letter.txt`: A text file containing the letter template with a placeholder `[name]` to be replaced by actual names.
- `Output/ReadyToSend/`: Directory where the personalized letters are saved. Each letter is named `letter_for_<name>.txt` or `letter_for_<name>.docx`.


