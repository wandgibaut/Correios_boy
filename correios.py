from selenium import webdriver
import json

chrome = webdriver.Chrome()
filepath = 'encomendas.txt'

chrome.get('https://www2.correios.com.br/sistemas/rastreamento/resultado.cfm')
textarea = chrome.find_element_by_tag_name('textarea')
btnPesq = chrome.find_element_by_id('btnPesq')

encomendas = []
with open(filepath) as fp:
   line = fp.readline()
   while line:
       encomendas.append(line.strip())
       line = fp.readline()

for encomenda in encomendas:
    textarea.send_keys(encomenda)

btnPesq.click()
chrome.implicitly_wait(2)

answers = chrome.find_element_by_xpath('//*[@id="sroFormMultiResultado"]/table/tbody')

entrySetAnswer = answers.find_elements_by_tag_name('tr')
objectArr = []
for element in entrySetAnswer:
    entrySetInfo = element.find_elements_by_tag_name('td')
    correioObject = {
        "Objeto": entrySetInfo[0].text,
        "Info": entrySetInfo[1].text,
        "TimeStamp": entrySetInfo[2].text,
    }
    objectArr.append(correioObject)

for i in objectArr:
    print(i['Objeto'])
    print(i['Info'])
    print(i['TimeStamp']) 
    print('')

chrome.close()
print ('done!')