import time

def main():
    while True:
        def help_command():
            file_path = 'source/help_ppm.txt'

            try:
                # Open the file in read mode
                with open(file_path, 'r') as file:
                    # Read the contents of the file
                    file_contents = file.read()
                    print(file_contents)

            except FileNotFoundError:
                print(f"The file '{file_path}' does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

        def default_command():
            command = input(">> ")

            if command == ".help":
                help_command()
            elif command == ".exit":
                quit()
            else:
                print("error: '" + command + "' isn't a command")
        default_command()

if __name__ == "__main__":
    main()
