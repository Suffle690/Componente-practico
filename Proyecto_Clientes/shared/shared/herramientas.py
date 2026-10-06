def confirmar(mensaje):
    respuesta = input(mensaje + " (s/n): ")

    if respuesta.lower() == "s":
        return True

    return False


def es_email_valido(email):
    if "@" in email and "." in email:
        return True

    return False