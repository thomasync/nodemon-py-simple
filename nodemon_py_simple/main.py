import os
import time
import subprocess
import argparse

process = None

def execute_process(args) -> None:
    global process
    # Clear the console, if specified
    if args.clear:
        os.system("cls" if os.name == "nt" else "clear")

     # Kill the specified process, if specified
    if args.kill and process:
        process.kill()
        process.wait()

    # Execute the process
    process = subprocess.Popen(args.exec, shell=True)

def main():
    # Define the command line arguments and options
    parser = argparse.ArgumentParser(description="Watch a directory for file changes and execute a command")
    parser.add_argument("directory", help="The directory to watch")
    parser.add_argument("-e", "--extensions", help="A list of file extensions to watch, separated by commas")
    parser.add_argument("-k", "--kill", help="The process name of the process to kill when a file is modified or added", action="store_true")
    parser.add_argument("-c", "--clear", help="Clear the console before executing the command", action="store_true")
    parser.add_argument("exec", help="The command to execute when a file is modified or added")
    args = parser.parse_args()

    last_modified = {}

    # Traverse the directory and its subdirectories to find all existing files
    for root, dirs, files in os.walk(args.directory):
        for filename in files:
            # Skip files with the wrong extension, if specified
            if args.extensions and not filename.endswith(tuple(args.extensions.split(","))):
                continue

            path = os.path.join(root, filename)
            last_modified[path] = os.path.getmtime(path)

    # Execute the process once to start the process
    execute_process(args)

    # Loop indefinitely to watch for file changes
    while True:
        try:
            # Traverse the directory and its subdirectories again to find new files
            for root, dirs, files in os.walk(args.directory):
                for filename in files:
                    # Skip files with the wrong extension, if specified
                    if args.extensions and not filename.endswith(tuple(args.extensions.split(","))):
                        continue

                    path = os.path.join(root, filename)

                    # Check if the file is new
                    if path not in last_modified:
                        # Add the new file to the dictionary and execute the command
                        last_modified[path] = os.path.getmtime(path)

                        # Execute the process
                        execute_process(args)

                    # Check if the file has been modified
                    elif os.path.getmtime(path) != last_modified[path]:
                        # Update the last modified time and execute the command
                        last_modified[path] = os.path.getmtime(path)

                        # Execute the process
                        execute_process(args)

            time.sleep(1)

        except KeyboardInterrupt:
            break

if __name__ == "__main__":   
    main()