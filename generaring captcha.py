from captcha.image import ImageCaptcha
image_info = ImageCaptcha(width=250,height=100)

captcha_text ='NAVEEN'
source =image_info.generate(captcha_text)
image_info.write(captcha_text, 'Captcha.png')