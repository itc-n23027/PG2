
import shelve
import pyperclip
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python mcb.py [save|list|delete] [keyword]")
        return

    with shelve.open('mcb') as mcb_shelf:
        if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
            mcb_shelf[sys.argv[2]] = pyperclip.paste()
        elif len(sys.argv) == 2:
            if sys.argv[1].lower() == 'list':
                pyperclip.copy(str(list(mcb_shelf.keys())))
                print("Keywords copied to clipboard.")
            elif sys.argv[1] in mcb_shelf:
                pyperclip.copy(mcb_shelf[sys.argv[1]])
                print(f"Keyword '{sys.argv[1]}' copied to clipboard.")
            elif sys.argv[1].lower() == 'delete':
                print("Usage: python mcb.py delete [keyword]")
        elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
            if sys.argv[2] in mcb_shelf:
                del mcb_shelf[sys.argv[2]]
                print(f"Keyword '{sys.argv[2]}' deleted.")
            else:
                print(f"Keyword '{sys.argv[2]}' not found.")

if __name__ == '__main__':
    main()
