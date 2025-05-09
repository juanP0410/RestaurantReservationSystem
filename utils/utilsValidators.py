# utils/Validators.py
def validar_email_unico(email, clientes):
    for cliente in clientes:
        if cliente.email == email:
            return False
    return True