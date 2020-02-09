# Correios_boy

Um programa simples baseado no [Selenium](https://selenium.dev/) para verificar o status de encomendas no site dos [Correios](https://www2.correios.com.br/sistemas/rastreamento/resultado.cfm).


## Uso
No arquivo **encomendas.txt**, escreva o código dos correios relativo a cada encomenda (um por linha), acrescido de ponto e virgula no final.
Ex:

OI777542982BR; 

LO359023013CN;

Com o arquivo **encomendas.txt** devidamento configurado, execute o script python de acordo com o seu Sistema Operacional. 
Ex:

$ python3 correios.py (Linux)

Alternativamente, caso o Sistema Operacional seja linux (ou qualquer outro que possa rodar arquivos *bash*), pode-se executar:

$ ./runCorreios.sh

Este script já faz o *source* do chromedriver deste repositório e executa o script python. Atente-se que é necessário dar permissão de execução neste segundo caso.


O repositório contém ainda um [ambiente virtual](https://docs.python.org/3/library/venv.html) já com o Selenium e uma pasta com o **chromedriver** necessário para o funcionamento correto.

## Requisitos
* Python 3
* [Selenium](https://selenium.dev/)
* Google Chrome
