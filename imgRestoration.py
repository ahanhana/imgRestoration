from tkinter import filedialog
from PIL import Image, ImageEnhance


def open_file_dialog():
    file_path = filedialog.askopenfilename()
    # 在这里添加代码，处理文件路径
    print("选择的文件路径：", file_path)
    return file_path


# 打开原图像
# img = Image.open('image.png')
filePath = open_file_dialog()
img = Image.open(filePath)
# 设置增强因子
factor = float(input('请输入增强系数(1.0~99.9):'))

enhancer = ImageEnhance.Sharpness(img)

# 增强图片
img_enhanced = enhancer.enhance(factor)

# 保存增强后的图像
arr = filePath.split('/')
i=0
fileDir=''
len = len(arr)
while i < len-1:
    fileDir += arr[i]+'/'
    i += 1

img_enhanced.save(fileDir+'output'+factor.__str__()+arr[len-1])
print('输出文件为:'+fileDir+'output'+factor.__str__()+arr[len-1])
