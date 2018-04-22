# 批量下载图片整理文件批量修改文件名

#发起请求
import requests
from PIL import Image
from io import BytesIO

url = 'http://desk.fd.zol-img.com.cn/t_s960x600c5/g5/M00/08/0B/ChMkJlbZOHGIQPkpAA-T3dOxKtsAAMhjwHmJocAD5P1844.jpg'
resp = requests.get(url)
print(resp)

#以二进制的数据创建图片，并保存下来
pic = Image.open(BytesIO(resp.content))
pic.save('2.jpg', 'jpeg')




