#importing needed libraries
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
pr={}  # dictionaries to store prices,raitings
ra={}
l=[]
count=0  # variable to count sample size
avgpr={}  # dictionaries to store average datas
avgra={}
names=dict()
#Opening the url which is to be scraped
url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&as-pos=1&as-type=HISTORY"
#Opening the url
r=requests.get(url) 
htmlcon=r.content
#using BeautifulSoup to take html script from web
soup=BeautifulSoup(htmlcon,'html.parser')
# Searching and picking the require data
for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}): #Opening an anchor tag
    name=a.find('div', attrs={'class':'_4rR01T'}) #searching for brand
    f=name.text
    s=f.find(' ')                                 # data manipulation
    f=f[0:s]
    names[f]=names.get(f,0)+1
    rating=a.find('div', attrs={'class':'_3LWZlK'})
    price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    d=rating.text
    p=price.text
    j=p.find(',')
    p=p[1:j]+p[j+1:]
    pr[f]=pr.get(f,0)+int(p)
    ra[f]=ra.get(f,0)+float(d)
    count=count+1
# Data Analysis starts here
print("This programme picks some data of Smartphones from flipkart.com and analyse it") 
print("In a random Sample of",count,"Smartphones split-up is as:")
# Plotting the graph for Sample Data
plt.title("Sample Statistics")
plt.xlabel("Brand")
plt.ylabel("No. of Smartphones")
key=names.keys()
value=names.values()
plt.bar(key,value)
plt.show()
plt.close()
# Calculating averages
for i in names:
    avgpr[i]=pr[i]/names[i]
    avgra[i]=ra[i]/names[i]
# Plotting graph for average prices
plt.title(" Average Prices ")
plt.xlabel("Brand")
plt.ylabel(" Price ")
key=avgpr.keys()
value=avgpr.values()
plt.bar(key,value)
for k,v in avgpr.items():
    l.append((v,k))
l.sort()
print()
print("The cheapest Smartphone Brand is: ",l[0][1])
print("The most expensive Smartphone Brand is: ",l[-1][1])
plt.show()
plt.close()
l.clear()
# Plotting graph for Customer reviews
plt.ylim(4.0,4.4)
plt.title(" Ratings ")
plt.xlabel("Brand")
plt.ylabel("Customer Reviews")
key=avgra.keys()
value=avgra.values()
plt.bar(key,value)
for k,v in avgra.items():
    l.append((v,k))
l.sort()
print()
print("The lowest preferred Smartphone Brand (A/c to customers) is: ",l[0][1])
print("The most preferred Smartphone Brand (A/c to customers) is: ",l[-1][1])
plt.show()




