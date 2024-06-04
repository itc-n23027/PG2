import re

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def replace_keywords(text):
    keywords = re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB', text)
    
    for keyword in keywords:
        replacement = input(f'Enter a {keyword.lower()}: ')
        text = text.replace(keyword, replacement, 1)
    
    return text

def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    text = read_file(input_filename)
    
    new_text = replace_keywords(text)
    
    print('\nResult:')
    print(new_text)
    
    write_file(output_filename, new_text)

if __name__ == '__main__':
    main()
