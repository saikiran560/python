# copyfile.py

def copy_file_content(source_filename, destination_filename):
    try:
        # Open the source file in read mode
        with open(source_filename, 'r') as source_file:
            # Read the contents of the source file
            file_content = source_file.read()

        # Open the destination file in write mode
        with open(destination_filename, 'w') as destination_file:
            # Write the contents to the destination file
            destination_file.write(file_content)

        print(f"Content copied from '{source_filename}' to '{destination_filename}' successfully.")

    except FileNotFoundError:
        print("One or both of the specified files were not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user for file names
    source_file_name = input("Enter the name of the source file: ")
    destination_file_name = input("Enter the name of the destination file: ")

    # Copy the contents of the source file to the destination file
    copy_file_content(source_file_name, destination_file_name)
