def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    # print(text)
    word_count = count_words(text)
    # print(f"There are {word_count} words in this text.")
    char_count = count_characters(text)
    # print(char_count)
    chars_in_sorted_list = chars_dict_to_sorted_list(char_count)

    print(f"\nHere is the analysis of {book_path}:")
    print("************************************************")
    print(f"\nThere are {word_count} words in this text.\n")
    
    for item in chars_in_sorted_list:
        if not item["char"].isalpha():
            continue
        # print(f"Character: '{item['char']}', Count: {item['num']}")
        print(f"Character: '{item['char']}' appears {item['num']} times")


def get_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
    text_words = text.split()
    return len(text_words)

def count_characters(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = [{"char": char, "num": num} for char, num in num_chars_dict.items()]
    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list

main()