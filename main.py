path = "books/frankenstein.txt"

def main():
    with open(path) as f:
        file_contents = f.read()
        return file_contents
def count_words():
    return len(main().split())
def count_letters():
    lowercase_letters = main().lower()
    temp_dic = {}
    final_list = []

    for letter in lowercase_letters:
        if letter.isalpha() == True:
            if letter in temp_dic:
                temp_dic[letter] += 1
            else:
                temp_dic[letter] = 1

    for i in temp_dic:
        new_dic = {}
        new_dic["letter"] = i
        number = temp_dic[i]
        new_dic["number"] = number
        final_list.append(new_dic)

    return final_list
def report():
    dic = count_letters()
    def sort_on(dic):
        return dic["number"]
    dic.sort(reverse=True, key=sort_on)

    final_report = f"--- Begin report of {path} --- \n"

    for i in dic:
        let = i["letter"]
        num = i["number"]
        line = f"The {let} character was found {num} times \n"
        final_report += line

    final_report += "--- End report ---"

    print(final_report)

report()