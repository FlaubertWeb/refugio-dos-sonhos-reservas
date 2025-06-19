import flet as ft

def main(page: ft.Page):
    quartos = [
        {"Tipo": "Simples", "Numero": 101, "Disponivel": True},
        {"Tipo": "Luxo", "Numero": 102, "Disponivel": False},
        {"Tipo": "Executiva", "Numero": 103, "Disponivel": True}
    ]

    page.title = "Reservas para um Hotel Boutique"
    page.window.width = 500
    page.window.max_width=500
    page.window.height = 600
    page.horizontal_alignment = "center"
    page.vertical_alignment = "top"

    titulo = ft.Text("🏨 Reservas para um Hotel Boutique", size=20)
    lista_quartos = []

    for quarto in quartos:
        status = "✅ Disponível" if quarto["Disponivel"] else "❌ Indisponível"
        lista_quartos.append(
            ft.Row([
                ft.Text(f"Quarto {quarto['Numero']} ({quarto['Tipo']}) : {status}", size=18),
                ft.ElevatedButton("Reservar", disabled=not quarto["Disponivel"])
            ],
            alignment="spaceBetween")
        )

    info_cliente = ft.ElevatedButton("Informações de clientes")
    gerenciar_reservas = ft.ElevatedButton("Gerenciar reservas")

    page.add(
        ft.Container(
            content=ft.Column([
                titulo,
                *lista_quartos,
                ft.Row([info_cliente, gerenciar_reservas], alignment="center")
            ],
            horizontal_alignment="center",
            spacing=20),
            padding=20,
            width=500,
            alignment=ft.alignment.center
        )
    )

ft.app(target=main)
