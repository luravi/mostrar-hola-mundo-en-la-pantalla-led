def on_forever():
    basic.show_string("Hola Mundo!")
    serial.write_line("Este texto aparece en la consola")

basic.forever(on_forever)
