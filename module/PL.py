from PIL import Image
im=Image.open('1.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('1-副本.jpg','JPEG')
