import flet as ft
import random

class KPOJatek(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.jatekos_valasztas = None
        self.szamitogep_valasztas = None
        self.eredmeny = None

    def valasztas(self, valasztas):
        self.jatekos_valasztas = valasztas
        self.szamitogep_valasztas = random.choice(["ko", "papir", "ollo"])
        self.nyertes_meghatarozas()
        self.update()

    def nyertes_meghatarozas(self):
        valasztasok = {
            "ko": {"ollo": "nyertes", "papir": "vesztes"},
            "papir": {"ko": "nyertes", "ollo": "vesztes"},
            "ollo": {"papir": "nyertes", "ko": "vesztes"},
        }
        self.eredmeny = valasztasok[self.jatekos_valasztas][self.szamitogep_valasztas]
        if self.eredmeny == "nyertes":
            self.eredmeny = "Te nyertél!"
        elif self.eredmeny == "vesztes":
            self.eredmeny = "A számítógép nyert!"
        else:
            self.eredmeny = "Döntetlen!"

    def build(self):
        ko_gomb = ft.IconButton(
            icon=ft.icons.SPORTS_HANDBALL,
            icon_color=ft.colors.BLUE,
            icon_size=48,
            on_click=lambda _: self.valasztas("ko"),
        )
        papir_gomb = ft.IconButton(
            icon=ft.icons.FEED_OUTLINED,
            icon_color=ft.colors.BLUE_GREY,
            icon_size=48,
            on_click=lambda _: self.valasztas("papir"),
        )
        ollo_gomb = ft.IconButton(
            icon=ft.icons.CONTENT_CUT,
            icon_color=ft.colors.YELLOW,
            icon_size=48,
            on_click=lambda _: self.valasztas("ollo"),
        )

        jatekos_kep = ft.Image(src=f"/icons/{self.jatekos_valasztas or 'placeholder'}.png")
        szamitogep_kep = ft.Image(src=f"/icons/{self.szamitogep_valasztas or 'placeholder'}.png")

        eredmeny_szoveg = ft.Text(self.eredmeny or "Válassz!", style=ft.TextThemeStyle.HEADLINE_MEDIUM)

        return ft.Column(
            width=300,
            height=500,
            controls=[
                ft.Text("Kő-papír-olló", style=ft.TextThemeStyle.HEADLINE_SMALL),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[ko_gomb, papir_gomb, ollo_gomb],
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[jatekos_kep, ft.VerticalDivider(width=1), szamitogep_kep],
                ),
                eredmeny_szoveg,
            ],
        )

def main(page):
    page.title = "Kő-papír-olló"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 300
    page.window_height = 500
    page.update()

    jatek = KPOJatek()
    page.add(jatek)

ft.app(target=main)