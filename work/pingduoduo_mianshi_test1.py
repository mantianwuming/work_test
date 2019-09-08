import cv2
from PIL import Image

class Solution:
    def cal_g(self,hist, threshold):
        n0 = 0
        n1 = 0
        total = 0
        for i in range(256):
            total += hist[i]
            if i <= threshold:
                n0 += hist[i]
            else:
                n1 += hist[i]
        w0 = n0 / total
        w1 = n0 / total
        sum = 0
        sum0 = 0
        sum1 = 0
        for i in range(256):
            sum += hist[i] * i
            if i <= threshold:
                sum0 += hist[i] * i
            else:
                sum1 += hist[i] * i
        mean_val = sum / total
        mean_val0 = sum0 / n0
        mean_val1 = sum1 / n1
        g = w0 * (mean_val0 - mean_val) ** 2 + w1 * (mean_val1 - mean_val) ** 2
        # g = w0 * w1 * (mean_val0 - mean_val1) ** 2
        return g

    def otsu(self, hist):
        max_g = 0
        threshold = 0
        for i in range(256):
            g = self.cal_g(hist, i)
            if g > max_g:
                max_g = g
                threshold = i
        return threshold
    
    def get_hist(self, img_path):
        image = cv2.imread(img_path, 0)
        hist = [0 for _ in range((256))]
        for i in range(len(image)):
            for j in range(len(image[0])):
                num = image[i][j]
                hist[num] += 1
        return hist
    
    def RGB2Gray(self, img_path, newFilePath):
        img = Image.open(img_path)
        img = img.convert('L')
        img.save(newFilePath)
    
    def get_binary_image(self, img_path, threshold):
        img = cv2.imread(img)
        for i in range(len(img)):
            for j in range(len(img[0])):
                if img[i][j] > threshold:
                    img[i][j] = 255
                else:
                    img[i][j] = 0
        cv2.save('test.jpg', img)

if __name__ == "__main__":
    img_path = './test_for_otsu.jpg'
    s = Solution()
    s.RGB2Gray(img_path, './test1.jpg')
    hist = s.get_hist('./test1.jpg')
    threshold = s.otsu(hist)
    s.get_binary_image('./test1.jpg', threshold)






