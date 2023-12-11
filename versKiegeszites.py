def megnyitas():
    beFajl = open("fajlok/KariVers.txt", "r", encoding="utf-8")
    vers = beFajl.read()
    beFajl.close()

    kiFajl = open("fajlok/KariVers2.txt", "w", encoding="utf-8")
    kiFajl.write(vers)
    kiFajl.write("\n\nTiszta öröm tüze átég")
    kiFajl.write("\na szemeken, a harangjáték")
    kiFajl.write("\nszól, éjféli üzenet:")
    kiFajl.write("\nKis Jézuska született!")
