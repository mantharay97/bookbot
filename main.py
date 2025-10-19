def main():

    def get_book_text():
        with open("/home/mantharay/workspace/github.com/mantharay97/bookbot/books/frankenstein.txt") as f:
            file_contents = f.read()
        return file_contents
    
main()		