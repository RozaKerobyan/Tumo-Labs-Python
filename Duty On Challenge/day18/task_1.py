def get_words():
    user_prompt = input("Enter words separated by commas: ")
    words = user_prompt.split(',')
    return words

def get_positions():
    position_1 = int(input('pos1= ')) - 1
    position_2 = int(input('pos2= ')) - 1
    return position_1, position_2

def swap_elements(words, pos1, pos2):
    words[pos1], words[pos2] = words[pos2], words[pos1]
    return words

def main():
    words = get_words()
    pos1, pos2 = get_positions()
    words = swap_elements(words, pos1, pos2)
    print(words)

if __name__ == "__main__":
    main()
