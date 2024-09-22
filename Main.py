def remove_dubs_lines(input_file, output_file):
    """
    Removes lines containing the word "dubs" from the input text file and writes the modified content to the output file.

    Args:
        input_file (str): The name of the input text file.
        output_file (str): The name of the output text file.
    """

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if "dubs" not in line.lower():  # Case-insensitive check
                    outfile.write(line)

        print(f"Lines containing 'dubs' have been removed. Output saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")

if __name__ == "__main__":
    input_file = input("Enter the name of the input text file: ")
    output_file = input("Enter the desired name for the output file: ")

    remove_dubs_lines(input_file, output_file)
