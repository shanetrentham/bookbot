def get_word_count(text):
    words = text.split()
    return len(words)

def get_count_of_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
def sort_dictionary(characters):
    return sorted(characters.items(), key=lambda item: item[1], reverse=True)