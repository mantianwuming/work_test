def cal_auc(label, prediction):
    positive = [i for i in range(len(label)) if label[i] == 1]
    negative = [i for i in range(len(label)) if label[i] == 0]
    auc = 0
    for i in positive:
        for j in negative:
            if prediction[i] > prediction[j]:
                auc += 1
            elif prediction[i] == prediction[j]:
                auc += 0.5
    auc /= (len(positive) * len(negative))
    return auc

n = int(input())
label = []
prediction = []
for i in range(n):
    l, p = map(float, input().split())
    label.append(l)
    prediction.append(p)
auc = cal_auc(label, prediction)
auc = round(auc, 2)
print(auc)