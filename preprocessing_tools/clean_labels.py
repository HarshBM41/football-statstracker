import os

def replace_first_word_in_files(folder_path, new_class = 2):
    # Iterate through all files in the given folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
            
        # Open the file and read the content
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Check if file has any lines
        if lines:
            # Split the first line into words and replace the first word
            first_line_words = lines[0].split()
            if first_line_words:
                first_line_words[0] = new_class  # Replace the first word with the new word
                lines[0] = ' '.join(first_line_words) + '\n'  # Reconstruct the first line

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)

# Example usage
folder_path = 'path_to_your_folder'  # Replace with the path to your folder
replace_first_word_in_files(folder_path='sample_data\SNMOT-060\labels\sample_public', new_class=2)