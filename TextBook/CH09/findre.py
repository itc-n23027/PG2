import os
import re

def search_in_files(directory, pattern):
    regex = re.compile(pattern)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for line_number, line in enumerate(lines, 1):
                        if regex.search(line):
                            print(f'File: {file_path}, Line {line_number}: {line.strip()}')

def main():
    directory = input('Enter the directory path: ')
    pattern = input('Enter the regex pattern: ')
    
    search_in_files(directory, pattern)

if __name__ == '__main__':
    main()
