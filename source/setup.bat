@echo off

rem Criando ambiente virtual
python -m venv venv

rem Ativando ambiente virtual
call venv\Scripts\activate.bat

rem Instalando pacotes necessários
pip install -r requirements.txt

deactivate