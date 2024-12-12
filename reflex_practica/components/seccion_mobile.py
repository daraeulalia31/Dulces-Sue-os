import reflex as rx
from ..components.mi_button import mi_button_p
def seccion_mobile()->rx.Component:
  return rx.mobile_and_tablet(
    rx.heading(
      "Elige, Selecciona y Compra el mejor Ordenador",
      color="#eff9ff",
      size="8",
      align="center"
    ),
    rx.heading(
      "con ",
      rx.text.em("PC STORE",color="#92dafe"),
      color="#eff9ff",
      size="9",
      align="center"
    ),
    rx.hstack(
      rx.text(rx.text.em("Upskill",color="#92dafe",weight="bold")," ¡Bienvenido a Pc Store! Tu destino para la mejor selección de componentes y periféricos para PC. Ya sea que estés buscando construir tu PC de ensueño, actualizar tu sistema actual o simplemente necesitas un nuevo ratón o teclado, tenemos todo lo que necesitas. Explora nuestra amplia gama de productos de las marcas más reconocidas y disfruta de precios competitivos y un servicio al cliente excepcional.",size="5",color="#eff9ff",text_align="center"),
    ),
    rx.vstack(
      rx.link(mi_button_p("user","Inicia Sesion"),href="/login"),
      margin_top="4em",
      align="center"
    ),
    width="90vw",
  )