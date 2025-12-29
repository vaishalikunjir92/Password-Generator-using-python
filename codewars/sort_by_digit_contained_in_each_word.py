def order(sentence):
    if not sentence:
        return ""
    words = sentence.split()

    # Sort by the digit contained in each word
    sorted_words = sorted(words, key=lambda w: int("".join(ch for ch in w if ch.isdigit())))

    return " ".join(sorted_words)


print(order("is2 Thi1s T4est 3a"))