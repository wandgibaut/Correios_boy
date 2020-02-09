# Correios_boy

Um programa simples baseado no [Selenium](https://selenium.dev/) para verificar o status de encomendas no site dos correios.


## Uso
No arquivo **encomendas.txt**, escreva o código dos correios relativo a cada encomenda (um por linha), acrescido de ponto e virgula no final.
Ex:

OI777542982BR; 

LO359023013CN;

Com o arquivo **encomendas.txt** devidamento configurado, execute o script python de acordo com o seu Sistema Operacional. 
Ex:

$ python3 correios.py (Linux)

O repositório contém ainda um [ambiente virtual](https://docs.python.org/3/library/venv.html) já contendo o Selenium.

## Requisitos
* Python 3
* [Selenium](https://selenium.dev/)
