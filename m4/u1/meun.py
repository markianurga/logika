from PIL import Image, ImageFilter

with Image.open("1.jpg" ) as original :
    coler = original.convert("L")
    #coler.show()
    #original.show()
    coler.save('coler_1.jpg')
    
    blur_coler = coler.filter(ImageFilter.BLUR)
    blur_coler.save('blur_coler_1.jpg')
    
    blur_2 = original.filter(ImageFilter.BLUR)
    blur_2.save('blur_2_1.jpg')
    
    left = original.transpose(Image.ROTATE_90)
    left.save('lft_orl_1.jpg')
    
    right = original.transpose(Image.ROTATE_270)
    right.save('rt_orl_1.jpg')
    
    
 #   print(original.size)
  #  print(original.format)
   # print(original.mode)
  