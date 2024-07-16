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
        
    def main_image(e):
        main_image.width=400
        main_image.height=400

        main_image.update()


    product_images = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        main_image := ft.Image(
                        src="https://fonefazy.com/cdn/shop/files/rn-image_picker_lib_temp_95cde144-585d-42fb-9afa-32ff28268ae2_600x.webp?v=1703374169",
                        width=350,
                        height=500,
                        # fit=ft.ImageFit.CONTAIN, # Tratamento de imagem caso a imagem for menor
                    ),
                    ]
                ),
                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src="https://fonefazy.com/cdn/shop/files/rn-image_picker_lib_temp_95cde144-585d-42fb-9afa-32ff28268ae2_600x.webp?v=1703374169",
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src="https://fonefazy.com/cdn/shop/files/rn-image_picker_lib_temp_4a97edc2-86c6-4dab-af00-ac533e3b607a_600x.jpg?v=1703374169",
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                        # Precisa de um scroll para que possa passar mais imagens do produto
                        #
                        # ft.Container(
                        #     image_src="https://fonefazy.com/cdn/shop/files/rn-image_picker_lib_temp_ff66ea49-7f61-43ba-8d60-38fbfa9875ef_500x.jpg?v=1703374169",
                        #     width=80,
                        #     height=80,
                        #     opacity=0.5,
                        #     on_click=change_main_image
                        # ),
                         ft.Container(
                            image_src="https://fonefazy.com/cdn/shop/files/rn-image_picker_lib_temp_a50163d7-7966-4130-ae3f-bf239b526993_500x.jpg?v=1703374169",
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src="https://fonefazy.com/cdn/shop/files/rn-image_picker_lib_temp_2dd12197-a156-4ec1-a0b2-6bb9da5249ca_700x.webp?v=1703374169",
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
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='FONES DE OUVIDO BLUETOOTH',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    value='Fone de Ouvido T6 TWS Sport',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),
                ft.Text(
                    value='Esportivos',
                    color=ft.colors.GREY,
                    italic=True,
                ),
                ft.ResponsiveRow(
                    columns=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm': 6}, # XS quando ele for menor (Tela de ANDROID) e SM quando ele for maior (Tela de PC)
                            value='R$ 149',
                            color=ft.colors.WHITE,
                            size= 30,
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm': 6},
                            spacing=5,
                            wrap=False,
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER if _ < 4 else ft.colors.WHITE,
                                ) for _ in range(5)  # ' _ ' significa um elemento
                            ]
                        )
                    ]
                ),
                ft.Tabs(
                    selected_index=0,
                    height=250,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Explore a liberdade sonora sem comprometer o estilo com nosso Fone de Ouvido Bluetooth equipado com um prático Display Indicador de Bateria. Projetado para oferecer uma experiência auditiva sem limites, este fone de ouvido combina funcionalidade avançada e design moderno, proporcionando uma maneira elegante de aproveitar sua música, podcasts e chamadas favoritas.',
                                    color=ft.colors.GREY,
                                )
                            )
                        ),
                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Conexão Bluetooth Descomplicada Liberte-se dos fios embaraçosos com a conectividade Bluetooth de última geração. Emparelhar seu dispositivo é rápido e fácil, permitindo que você mergulhe na música sem problemas. Qualidade Sonora Excepcional. Prepare-se para uma experiência auditiva cativante. Com drivers de alta qualidade, estes fones de ouvido oferecem um som equilibrado e envolvente, destacando cada nota e batida com clareza impressionante.',
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
                                ft.dropdown.Option(text='Preto'),
                                ft.dropdown.Option(text='Branco'),
                                ft.dropdown.Option(text='Verde'),
                                ft.dropdown.Option(text='Rosa'),
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
            ]
        ),
    )

    
    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.CENTER,
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