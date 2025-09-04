try:
    print("Texto con formato".format())

except Exception as e:
    e.add_note("Ha ocurrido un error")
    print(e)