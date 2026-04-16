import sys
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        content = get_book_text(book_path)
        num_words = get_num_words(content)
        chars_dict = get_chars_dict(content)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
        print_report(book_path, num_words, chars_sorted_list)
        sys.exit(0)


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()
sys.exit(1)
