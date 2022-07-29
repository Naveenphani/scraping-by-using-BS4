# scraping-by-using-BS4
#connecting Mysql, Bypass captcha using python(in jupyter

#....................SCRAPING BY USING BS4 (PYTHON)


from bs4 import BeautifulSoup 
import requests 
import csv
import pandas as pd



Product_Title= [] # Create a list to store the descriptions
Product_Image_URL=[]
Price_of_the_Product=[]
Product_Details=[]
Storage=[]
Display=[]
Camera=[]
Chip_Processor=[]
Warranty=[]


pages = list(range(1,21))
for page in pages:
  req = requests.get("https://www.flipkart.com/search?q=latest+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=latest+mobiles%7CMobiles&requestId=689fd316-7863-4300-9b01-9ca689dad956&as-searchtext=latest&sort=price_desc&page={}".format(page)).text  # URL of the website which you want to scrape
  #content = req.content # Get the content
  soup = BeautifulSoup(req,'html.parser')
  #print(soup.prettify())

  desc = soup.find_all('div' , class_='_4rR01T')
  for i in range(len(desc)):
        Product_Title.append(desc[i].text)
  len( Product_Title)

  descq = soup.find_all('div' , class_='_30jeq3 _1_WHN1')
  for i in range(len(descq)):
        Price_of_the_Product.append(descq[i].text)
  len(Price_of_the_Product)

  descf = soup.find_all('img', class_='_396cs4 _3exPp9')
  for i in range(len(descf)):
        Product_Image_URL.append(descf[i]['src'])
  len(Product_Image_URL)
    
  Product_Details=soup.find_all('li',class_='rgWa7D')
  for i in range(0,len(Product_Details)):
    p=Product_Details[i].text 
    if("ROM"in p): 
      Storage.append(p)
    elif("Display"in p): 
      Display.append(p)
    elif("Camera"in p):
        Camera.append(p)
    elif("Chip Processor"in p):
      Chip_Processor.append(p)
    elif("Warranty"in p):
      Warranty.append(p)
    len(Rom)
    len(Display)
    len(Camera)
    len(Chip_Processor)
    len(Warranty)



print(len(Product_Title))
print(len(Price_of_the_Product))
print(len(Product_Image_URL))
print(len(Storage))
print(len(Display))
print(len(Camera))
print(len(Chip_Processor))
print(len(Warranty))





df= pd.DataFrame()
df['Product_Titles']=Product_Title
df['Price_of_the_Product']=Price_of_the_Product
df['Product_Image_URL']=Product_Image_URL
df['Storage']=Storage
df['Display']=Display[slice(480)]
df['Camera']=Camera[slice(480)]
#df['Chip_Processor']=Chip_Processor[slice(480)]
#df['Warranty']=Warranty[slice(480)]
df.to_csv('naveenpersonal.csv')# Finally merging all the features into a single dataframe



dataset = pd.DataFrame(data = df)


dataset




df=pd.read_csv('naveenpersonal.csv')




df.shape





