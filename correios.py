# MIT License
#
# Copyright (c) 2020 Wandemberg Gibaut
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
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
