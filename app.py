
# Imagine que você foi contratado para desenvolver um sistema inovador de
# gerenciamento de reservas para um hotel boutique em uma cidade turística.

# O hotel, conhecido como "Refúgio dos Sonhos"

# , precisa de um sistema que
# permita gerenciar a disponibilidade dos quartos, as reservas dos hóspedes e
# os dados dos clientes de forma eficiente e intuitiva.

# Sua missão é criar uma aplicação interativa que atenda a essas necessidades
# utilizando Programação Orientada a Objetos (POO) e a biblioteca Flet para
# a interface gráfica.

#___________________________________________________________________________________________

# Utilize o Flet para construir uma interface gráfica que contenha as seguintes estruturas:

# Tela de visualização de reservas:
# Apresente uma lista de reservas existentes com a
# opção de cancelar reservas específicas.

# Tela inicial:
# Exiba uma lista de quartos e suas respectivas
# disponibilidades.
# Inclua botões para realizar reservas, consultar
# informações de clientes e gerenciar reservas.

# Formulário de reserva:
# Permita que o usuário escolha o cliente, o quarto e
# as datas desejadas para criar uma nova reserva.

# Gerenciamento de clientes:
# Inclua uma tela para visualizar, adicionar e editar
# informações dos clientes.

import flet as ft
from model import *

def main(page:ft.Page):
    pass
 
if __name__=="__main__":
    ft.app(target=main)


