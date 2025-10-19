def count_words(text):
    return len(text.split())

def count_characters(text):
    chr_counts = {}
    for char in text:
        char = char.lower()
        if char in chr_counts:
            chr_counts[char] += 1
        else:
            chr_counts[char] = 1
    return chr_counts