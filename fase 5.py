

peliculas_estreno = [
    {
        "accion": {
            "mortal kombat 2": "6 de mayo de 2026",
            "amos del universo": "5 de junio de 2026",
            "avengers:doomsday": "18 de diciembre de 2026",
            "spider-man:brand new day": "1 de enero de 2027",
            "aguas mortales": "1 de enero de 2027"
        }
    },
    {
        "ciencia ficcion": {
            "project hail mary": "20 de marzo de 2026",
            "star wars: the mandalorian y grogu": "21 de  de 2026",
            "la odisea(disclosure day)": "12 junio de 2026",
            "super girl: woman of tomorrow": "1 de enero de 2027",
            "dune: parte tres": "1 de enero de 2027"
        } 
    },
    {
        "drama": {
            "a complete unknown": "1 de enero de 2025",
            "michael": "24 de abril de 2026",
            "the drama": "1 de junio de 2026",
            "peaky blinders: the movie": "1 de junio de 2026",  
        }
    },
    {
        "comedia": {
            "letras robadas ": "4 junio de 2026",
            "toy story 5": "18 de junio de 2026",
            "minions 3": "1 de diciembre de 2026",
            "scary movie 6": "1 de diciembre de 2026",
            "coyote vs acme": "1 de diciembre de 2026"
        }
    },
    {
        "terror": {
            "el hombre lobo": "1 de enero de 2025",
            "backrooms": "28 de mayo de 2026",
            "evil dead burn(posesion infernal en llamas )": "10 julio de 2026",
            "nosferatu": "1 de marzo de 2026",
            "return to silent hill": "1 de marzo de 2026"
        }
    }
]


def mostrar_catalogo():
    print("------ Estrenos -----")
    print()
    for categoria in peliculas_estreno:
        for tipo, peliculas in categoria.items():
            print(tipo.title())
            for index, (titulo, fecha) in enumerate(peliculas.items(), start=1):
                print(f"  {index}. {titulo} - {fecha}")
            print("--" * 30)


def pedir_entero(mensaje, minimo, maximo):
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            valor = int(valor)
            if minimo <= valor <= maximo:
                return valor
        print(f"Por favor ingresa un número entre {minimo} y {maximo}.")


def calificar_por_categoria():
    calificaciones = {}
    for categoria in peliculas_estreno:
        for tipo, peliculas in categoria.items():
            print(f"\nCategoria: {tipo.title()}")
            for index, (titulo, fecha) in enumerate(peliculas.items(), start=1):
                print(f"  {index}. {titulo} - {fecha}")

            while True:
                respuesta = input(f"¿Quieres calificar películas de {tipo.title()}? (s/n): ").strip().lower()
                if respuesta in {"s", "si", "sí", "n", "no"}:
                    break
                print("Por favor escribe 's' o 'n'.")

            if respuesta in {"n", "no"}:
                continue

            calificaciones[tipo] = {}
            for titulo, fecha in peliculas.items():
                print(f"\nCalifica: {titulo} ({tipo.title()}) - estreno: {fecha}")
                calificacion = pedir_entero("Calificación del 1 al 10: ", 1, 10)
                calificaciones[tipo][titulo] = calificacion

    return calificaciones


def mostrar_favoritas(calificaciones):
    if not calificaciones:
        print("No hay calificaciones para mostrar.")
        return

    print("\n----- Tus películas favoritas por categoría -----")
    for tipo, peliculas in calificaciones.items():
        if not peliculas:
            continue
        ordenadas = sorted(peliculas.items(), key=lambda item: item[1], reverse=True)
        print(f"\n{tipo.title()}")
        for titulo, valor in ordenadas:
            print(f"  {titulo}: {valor}/10")
        mejor = ordenadas[0]
        print(f"  -> Película favorita de {tipo.title()}: {mejor[0]} con {mejor[1]}/10")


def main():
    mostrar_catalogo()
    calificaciones = calificar_por_categoria()
    mostrar_favoritas(calificaciones)


if __name__ == "__main__":
    main()


