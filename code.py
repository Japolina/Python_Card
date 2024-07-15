import flet as ft

def main(page: ft.Page):
    page.theme_mode = "Dark",
    page.scroll = ft.ScrollMode.AUTO

    def change_main_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
                main_image.src = elem.image_src
            else:
                elem.opacity =0.5

        main_image.update()
        options.update()

    product_images = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := ft.Image(
                    src='https://imgs.ponto.com.br/1555947067/1xg.jpg',
                ),
                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='https://imgs.ponto.com.br/1555947067/1xg.jpg',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='https://http2.mlstatic.com/D_NQ_NP_942879-MLU71482713005_092023-0.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='https://http2.mlstatic.com/D_NQ_NP_908128-MLU72835305161_112023-0.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        )
                    ]
                ),
            ]
        )
    )

    product_details = ft.Container(
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/16,
        content=ft.Column(
            ft.Text(
                value='CADEIRAS',
                color=ft.colors.AMBER,
                weight=ft.FontWeight.BOLD,
            ),
            ft.Text(
                value='Poltrona amarela',
                color=ft.colors.WHITE,
                weight=ft.FontWeight.BOLD,
                size=30,
            ),
            ft.Text(
                value='Sala de estar',
                color=ft.colors.GREY,
                italic=True,
            ),
            ft.ResponsiveRow(
                columns=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        col={'xs': 12, 'sm': 6}, # XS quando ele for menor (Tela de ANDROID) e SM quando ele for maior (Tela de PC)
                        value='R$ 399',
                        color=ft.colors.WHITE,
                        size= 30,
                    ),
                    ft.Row(
                        ft.Icon(
                            name=ft.icons.STAR,
                            color=ft.colors.AMBER if _ < 4 else ft.colors.WHITE,
                        ) for _ in range(5)  # ' _ ' significa um elemento
                    )
                ]
            ),
            ft.Tabs(
                selected_index=0,
                height=150,
                indicator_color=ft.colors.AMBER,
                label_color=ft.colors.AMBER,
                unselected_label_color=ft.colors.GREY,
                tabs=[
                    ft.Tab(
                        text='Descrição',
                        content=ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Text(
                                value='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.',
                                color=ft.colors.GREY,
                            )
                        )
                    ),
                    ft.Tab(
                        text='Detalhes',
                        content=ft.Container(
                            padding=ft.padding.all(10),
                            content=ft.Text(
                                value='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s.',
                                color=ft.colors.GREY,
                            )
                        )
                    )
                ]
            ),
            ft.ResponsiveRow(
                columns=12,
                controls=[
                    ft.Dropdown(
                        col=6,
                        label='Cor',
                        label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                        border_color=ft.colors.GREY,
                        border_width=0.5,
                        options=[
                            ft.dropdown.Option(text='Amarelo'),
                            ft.dropdown.Option(text='Vermelho'),
                            ft.dropdown.Option(text='Cinza'),
                        ]
                    ),
                    ft.Dropdown(
                        col=6,
                        label='Quantidade',
                        label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                        border_color=ft.colors.GREY,
                        border_width=0.5,
                        options=[
                            ft.dropdown.Option(text=f'{num} unid') for num in range(1, 6)
                        ]
                    )
                ]
            ),
            
            ft.Container(expand=True),

            ft.ElevatedButton(
                width=900,
                text='Adicionar a lista de desejos',
                style=ft.ButtonStyle(
                    padding=ft.padding.all(20),
                    side={
                        ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                    },
                    bgcolor={
                        ft.MaterialState.HOVERED: ft.colors.WHITE
                    },
                    color={
                        ft.MaterialState.DEFAULT: ft.colors.WHITE,
                        ft.MaterialState.HOVERED: ft.colors.BLACK,
                    }
                )
            ),
            ft.ElevatedButton(
                width=900,
                text='Adicionar ao carrinho',
                style=ft.ButtonStyle(
                    padding=ft.padding.all(20),
                    side={
                        ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.AMBER)
                    },
                    bgcolor={
                        ft.MaterialState.DEFAULT: ft.colors.AMBER
                    },
                    color={
                        ft.MaterialState.DEFAULT: ft.colors.BLACK
                    }
                )
            )
        ),
    )

    
    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details
            ]
        )
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)