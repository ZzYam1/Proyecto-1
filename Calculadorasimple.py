from tkinter import *  # type: ignore

ventana = Tk()
ventana.title("Calculadora")
ventana.config(bg="#C7D2D2")

# Entrada

texto = Entry(ventana, font=("Arial 22"))
texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

uwu = 0

# Funcónamiento de los botones


def click_boton(valor):
    global uwu
    texto.insert(uwu, valor)
    uwu += 1


def ac():
    texto.delete(0, END)
    uwu = 0


def resultadosopr():
    problema = texto.get()
    resultadosopr = eval(problema)
    texto.delete(0, END)
    texto.insert(0, resultadosopr)
    uwu = 0


# Botones

punch1 = Button(ventana, text="1", width=5, height=2, command=lambda: click_boton(1))
punch1.config(bg="#FFFFFF")
punch2 = Button(ventana, text="2", width=5, height=2, command=lambda: click_boton(2))
punch2.config(bg="#FFFFFF")
punch3 = Button(ventana, text="3", width=5, height=2, command=lambda: click_boton(3))
punch3.config(bg="#FFFFFF")
punch4 = Button(ventana, text="4", width=5, height=2, command=lambda: click_boton(4))
punch4.config(bg="#FFFFFF")
punch5 = Button(ventana, text="5", width=5, height=2, command=lambda: click_boton(5))
punch5.config(bg="#FFFFFF")
punch6 = Button(ventana, text="6", width=5, height=2, command=lambda: click_boton(6))
punch6.config(bg="#FFFFFF")
punch7 = Button(ventana, text="7", width=5, height=2, command=lambda: click_boton(7))
punch7.config(bg="#FFFFFF")
punch8 = Button(ventana, text="8", width=5, height=2, command=lambda: click_boton(8))
punch8.config(bg="#FFFFFF")
punch9 = Button(ventana, text="9", width=5, height=2, command=lambda: click_boton(9))
punch9.config(bg="#FFFFFF")
punch0 = Button(ventana, text="0", width=13, height=2, command=lambda: click_boton(0))
punch0.config(bg="#FFFFFF")

borrar = Button(ventana, text="AC", width=5, height=2, command=lambda: ac())
borrar.config(bg="#E14B26")
parentesis1 = Button(
    ventana, text="(", width=5, height=2, command=lambda: click_boton("(")
)
parentesis1.config(bg="#FFFFFF")
parentesis2 = Button(
    ventana, text=")", width=5, height=2, command=lambda: click_boton(")")
)
parentesis2.config(bg="#FFFFFF")
decimal = Button(ventana, text=".", width=5, height=2, command=lambda: click_boton("."))
decimal.config(bg="#FFFFFF")
dividir = Button(ventana, text="÷", width=5, height=2, command=lambda: click_boton("/"))
dividir.config(bg="#FFFFFF")
multiplicar = Button(
    ventana, text="x", width=5, height=2, command=lambda: click_boton("*")
)
multiplicar.config(bg="#FFFFFF")
suma = Button(ventana, text="+", width=5, height=2, command=lambda: click_boton("+"))
suma.config(bg="#FFFFFF")
resta = Button(ventana, text="-", width=5, height=2, command=lambda: click_boton("-"))
resta.config(bg="#FFFFFF")
igual = Button(ventana, text="=", width=5, height=2, command=lambda: resultadosopr())
igual.config(bg="#FFFFFF")

# Posición de los botones

punch1.grid(row=4, column=0, padx=5, pady=5)
punch2.grid(row=4, column=1, padx=5, pady=5)
punch3.grid(row=4, column=2, padx=5, pady=5)
punch4.grid(row=3, column=0, padx=5, pady=5)
punch5.grid(row=3, column=1, padx=5, pady=5)
punch6.grid(row=3, column=2, padx=5, pady=5)
punch7.grid(row=2, column=0, padx=5, pady=5)
punch8.grid(row=2, column=1, padx=5, pady=5)
punch9.grid(row=2, column=2, padx=5, pady=5)
punch0.grid(row=5, columnspan=2, padx=5, pady=5)

borrar.grid(row=1, column=0, padx=5, pady=2)
parentesis1.grid(row=1, column=1, padx=5, pady=2)
parentesis2.grid(row=1, column=2, padx=5, pady=2)
decimal.grid(row=5, column=2, padx=5, pady=5)

dividir.grid(row=1, column=3, padx=5, pady=2)
multiplicar.grid(row=2, column=3, padx=5, pady=5)
suma.grid(row=3, column=3, padx=5, pady=5)
resta.grid(row=4, column=3, padx=5, pady=5)
igual.grid(row=5, column=3, padx=5, pady=5)

ventana.mainloop()
