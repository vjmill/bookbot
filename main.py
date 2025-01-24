with open("/root/workspace/github.com/vjmill/bookbot/books/frankenstein.txt") as f:
    file_contents = f.read()

def main():
    print(file_contents)

if __name__ == "__main__":
    main()

