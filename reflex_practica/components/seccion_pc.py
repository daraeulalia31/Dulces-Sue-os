import reflex as rx
from ..components.mi_button import mi_button_p
def seccion_pc()->rx.Component:
  return rx.desktop_only(
    rx.heading(
      "Bienvenido, Los mejores postres a buen precio",
      color="#eff9ff",
      size="8",
      align="center"
    ),
    rx.heading(
      "en ",
      rx.text.em("Dulces Sueños",color="#090b0f"),
      color="#eff9ff",
      size="9",
      align="center"
    ),
    rx.hstack(
      rx.text(rx.text.em("",color="#92dafe",weight="bold")," ¡En Dulces Sueños, horneamos felicidad. Cada bocado es una experiencia, creada con ingredientes de primera calidad y una pasión inigualable. Desde clásicos irresistibles hasta creaciones innovadoras, tenemos el postre perfecto para cualquier ocasión. ¡Visítanos y déjate llevar por el sabor!",size="5",color="#eff9ff",width="70vw"),
      rx.box(
        rx.image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPc4eeujGQ6FCLdqPGh-CbAV9VjGgRBH2WjA&s",alt="Imagen de app"),
        width="30vw"
      ),
      align="center"
    ),
    rx.vstack(
      rx.link(mi_button_p("user","Inicia Sesion"),href="/login"),
      margin_top="4em",
      align="center"
    ),
    width="70vw",
  )