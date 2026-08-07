text = input("Enter a paragraph:\n")
text = text.lower()

punctuation = ".,!?;:'\"()-[]{}"

for ch in punctuation:
    text = text.replace(ch, "")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord Frequency Analysis:")
for word in word_count:
    print(word, ":", word_count[word])

most_word = ""
most_count = 0

for word in word_count:
    if word_count[word] > most_count:
        most_count = word_count[word]
        most_word = word

if most_word != "":
    print("\nMost Frequent Word:")
    print(most_word, "->", most_count, "times")
