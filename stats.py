def count_words(book):
    result = book.split()
    return result

def count_char(book):
    words = count_words(book)
    result = {}
    count = 0
    for word in words:
        for char in word.lower():
            if char.isalpha():
                if char in result:
                    count += 1
                else:
                    result[char] = 0
                result[char] += 1
            else:
                continue
    return result

def report(word_list):
    new_list = []
    result = count_char(word_list)
    for elem in result.items():
        new_dict = {}
        new_dict["char"] = elem[0]
        new_dict["num"] = elem[1]
        new_list.append(new_dict)

    def sort_on(list):
        return list["num"]

    new_list.sort(reverse=True, key=sort_on)

    for elem in new_list:
        print(f"{elem["char"]}: {elem["num"]}")

