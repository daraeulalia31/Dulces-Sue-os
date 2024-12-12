import reflex as rx
from ..components.mi_button import mi_button_s
def navbar()->rx.Component:
  return rx.box(
    rx.desktop_only(
      rx.hstack(
        rx.heading("Dulces Sueños",color="#f026e1"),
        rx.hstack(
          rx.link(
            rx.icon("Instagram",color="#fd62e9")
          ),
          rx.link(
            rx.icon("Facebook",color="#17e8eb")
          ),
          rx.link(
            rx.icon("Twitter",color="#0f0bfd")
          ),
          rx.link(
            mi_button_s("user","Iniciar Sesion"),
            href="/login"
          ),
          justify="end",
          spacing="5",
          align_items="center"
        ),
        justify="between",
        align_items="center"
      ),
    ),
    rx.mobile_and_tablet(
      rx.hstack(
        rx.heading("Dulces Sueños",color="#eff9ff"),
        rx.hstack(
          rx.link(
            mi_button_s("user","Registrarse o Iniciar Sesion"),
            href="/login"
          ),
          justify="end"
        ),
        justify="between",
        align_items="center"
      )
    ),
    bg="#f9a4f2",
    #rx.color("#f586e0", 3),
    padding="1em",
    # position="fixed",
    # top="0px",
    # z_index="5",
    width="100%",
  )