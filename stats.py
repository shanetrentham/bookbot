def get_word_count(file_path):
    file_content = ""
    with open(file_path) as file:
        file_content = file.read()
    words = file_content.split()
    return len(words)

def get_count_of_characters(file_path):
    file_content = ""
    with open(file_path) as file:
        file_content = file.read()

    character_counts = {}
    lower = file_content.lower()
    for char in lower:
        if char in character_counts:
            character_counts[char] = character_counts[char] + 1
        else:
            character_counts[char] = 1
    return character_counts