import reflex as rx
from ..components.mi_button import mi_button_p
def seccion_mobile()->rx.Component:
  return rx.mobile_and_tablet(
    rx.heading(
      "Bienvenido, Los mejores postres a buen precio",
      color="#f026e1",
      size="8",
      align="center"
    ),
    rx.heading(
      "en ",
      rx.text.em("DULCES SUEÑOS",color="#f026e1"),
      color="#f026e1",
      size="9",
      align="center"
    ),
    rx.hstack(
      rx.text(rx.text.em("",color="#92dafe",weight="bold")," ¡En Dulces Sueños, horneamos felicidad. Cada bocado es una experiencia, creada con ingredientes de primera calidad y una pasión inigualable. Desde clásicos irresistibles hasta creaciones innovadoras, tenemos el postre perfecto para cualquier ocasión. ¡Visítanos y déjate llevar por el sabor.",size="5",color="#cc4cf3",text_align="center"),
    ),
    rx.vstack(
      rx.link(mi_button_p("user","Inicia Sesion"),href="/login"),
      margin_top="4em",
      align="center"
    ),
    width="90vw",
  )