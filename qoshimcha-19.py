class Film:
    def __init__(self, nom, rejissor, raqam, mavjud):
        self.nom = nom
        self.rejissor = rejissor
        self.raqam = raqam
        self.mavjud = mavjud

class Kinoteatr:
    def __init__(self, nom):
        self.nom = nom
        self.filmlar = []

    def film_qosh(self, film):
        self.filmlar.append(film)
        print(f"{film.nom} filmi kinoteatrga qo'shildi.")

    def filmni_ol(self, raqam):
        for film in self.filmlar:
            if film.raqam == raqam:
                if film.mavjud:
                    film.mavjud = False
                    return "Film ko'rsatildi"
                else:
                    return "Film mavjud emas"
        return "Film mavjud emas"

    def mavjud_filmlar(self):
        print("Mavjud filmlar:")
        for film in self.filmlar:
            if film.mavjud:
                print(f"Nom: {film.nom}, Rejissor: {film.rejissor}")

film1 = Film("Yulduzlar urushi", "J.J. Abrams", "001", True)
film2 = Film("Titanik", "James Cameron", "002", True)
film3 = Film("Matrix", "Lana va Lilly Wachowski", "003", False)

kinoteatr = Kinoteatr("Cinema City")

kinoteatr.film_qosh(film1)
kinoteatr.film_qosh(film2)
kinoteatr.film_qosh(film3)

kinoteatr.mavjud_filmlar()

print(kinoteatr.filmni_ol("001"))
print(kinoteatr.filmni_ol("003"))

kinoteatr.mavjud_filmlar()