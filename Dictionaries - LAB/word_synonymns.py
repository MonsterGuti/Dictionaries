number_of_words = int(input())
synonyms_dict = {}

for i in range(number_of_words):
    word = input()
    synonym = input()

    if word not in synonyms_dict:
        synonyms_dict[word] = []
    synonyms_dict[word].append(synonym)

for word in synonyms_dict:
    print(f"{word} - {', '.join(synonyms_dict[word])}")
