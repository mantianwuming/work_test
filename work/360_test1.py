words = input()

new_words = set(list(words))
# print(new_words)
def get_times(words, new_words):
    counts = []
    for i in new_words:
        count = 0
        for j in words:
            if i == j:
                count += 1
        counts.append(count)
    return counts

counts = get_times(words, new_words)
res = max(counts)
print(res)

