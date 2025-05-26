from stats import get_num_words, get_num_characters, sorted_dict
import sys




def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_text = get_book_text(sys.argv[1])
    total_words = get_num_words(book_text)

    num_chars = get_num_characters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    dict = sorted_dict(get_num_characters(book_text))
    for item in dict:
        if item["char"].isalpha():
            total = (item["char"] + ": " + str(item["num"]))
            print(total)
    
    print("============= END ===============")
    

if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)