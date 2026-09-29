import sys
from stats import counter
from stats import characters
from stats import chars_dict_to_sorted_list

def get_book_text(string: str) -> str:
    with open(string) as f:
        file_contents = f.read()
    return file_contents

def print_report(path: str, count: int, char_count: int):
    #print(path, count, char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for character, num in char_count:
        check = character.isalpha()
        if check == True:
            print(f"{character}: {num}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    tempText = get_book_text(path)
    temp = counter(tempText)
    #print(f"Found {temp} total words")
    tempChars = characters(tempText)
    tempChars_new = chars_dict_to_sorted_list(tempChars)
    #print(tempChars_new)
    print_report(path, temp, tempChars_new)

main()
