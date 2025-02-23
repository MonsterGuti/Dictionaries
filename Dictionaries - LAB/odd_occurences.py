words = input().split()

word_counts = {}

for word in words:
    word_lower = word.lower()
    word_counts[word_lower] = word_counts.get(word_lower, 0) + 1

odd_words = [word for (word, count) in word_counts.items() if count % 2 != 0]

print(" ".join(odd_words))
