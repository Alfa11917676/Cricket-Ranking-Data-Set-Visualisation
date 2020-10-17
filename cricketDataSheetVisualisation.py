import pandas as pandy

from bs4 import BeautifulSoup
from urllib.request import urlopen
ret=urlopen('https://www.espncricinfo.com/rankings/content/page/211271.html')

soup=BeautifulSoup(ret,'html.parser')

table_body=soup.find('div',{'class':'ciPhotoContainer'})
counter=0
head=soup.findAll('h3')
name=[]
for i in head:
    j=i.text
    name.append(j)

columns=['Position','Team','Matches','Points','Rating']

tr_list=soup.findAll('tr')
for i in tr_list:
    row=[]
    td_list=i.findAll('td')
    for j in td_list:
        a=j.text
        row.append(a)
        dict={}
        try:
            for k in range(len(yo.columns)):
                dict[yo.columns[k]]=row[k]
            yo=yo.append(dict,ignore_index=False)
        except:
            yo=pandy.DataFrame(columns=columns)
            table_name=name[counter]
            counter+=1
        yo.to_csv('C:\\Users\\ARNAB RAY\\Desktop\\PPts'+table_name+'.csv',index=False)
print("Done")