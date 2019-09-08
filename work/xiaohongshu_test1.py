import sys
sentence = sys.stdin.readline().strip()

def reverse_sentence(sentence):
    sentence = list(sentence)
    sentence.reverse()
    l = 0
    while l < len(sentence):
        while l < len(sentence)-1 and sentence[l] == ' ':
            l += 1
        r = l
        while r < len(sentence)-1 and sentence[r] != ' ':
            r += 1
        i = l
        j = r - 1
        if r == len(sentence) - 1:
            j = r
        while i < j:
            sentence[i], sentence[j] = sentence[j], sentence[i]
            i += 1
            j -= 1
        l = r+1
    new_sentence = ''.join(sentence)
    return new_sentence
    
new_sentence = reverse_sentence(sentence)
print(new_sentence)

