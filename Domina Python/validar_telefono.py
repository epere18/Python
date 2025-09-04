import phonenumbers

def validar_telefono(telefono_str, codigo_pais=None):
    try:
        telefono = phonenumbers.parse(telefono_str, codigo_pais)
        return phonenumbers.is_valid_number(telefono)
    except Exception as e:
        print(e)
        return False
    
valido = validar_telefono("+5491161756447")
print(valido)