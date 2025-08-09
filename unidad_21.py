"""Module providing a function printing python version."""

# /*
#  * UNIDAD 21: PETICIONES HTTP
#  * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
#  * una petición a la web que tú quieras, verifica que dicha petición
#  * fue exitosa y muestra por consola el contenido de la web.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
#  * terminal al que le puedas solicitar información de un Pokémon concreto
#  * utilizando su nombre o número.
#  * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
#  * - Muestra el nombre de su cadena de evoluciones
#  * - Muestra los juegos en los que aparece
#  * - Controla posibles errores
#  * /----------------------------------------------------------------------

# -----------------------------------------------------------------------------------
import os
import requests


def limpiar_consola():
    """Funcion para limpiar la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')
# -----------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------
# URL a la que realizaremos la peticion
URL = "https://www.google.com"

# Realizar la peticion GET
response_1 = requests.get(URL, timeout=10)

# Verificar que la peticion fue exitosa (codigo 200)
if response_1.status_code == 200:
    print("Peticion exitosa.")
    print("Contenido de la pagina: \n")
    print(response_1.text)  # Muestra el HTML completo
else:
    print(f"Error en la peticion. Codigo de estado: {response_1.status_code}")

limpiar_consola()
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# DESAFIO EXTRA:


def obtener_pokemon(pokemon):
    """Funcion para obtener los datos de un pokemon"""
    try:
        # Peticion a la API de Pokemon
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        datos = response.json()

        # Obtenemos los datos basicos
        nombre = datos["name"].capitalize()
        id_pokemon = datos["id"]
        peso = datos["weight"]
        altura = datos["height"]
        tipos = [t["type"]["name"].capitalize() for t in datos["types"]]

        # Juegos en los que aparece
        juegos = sorted({j["version"]["name"] for j in datos["game_indices"]})

        # Obtener cadena de evoluciones
        especies_url = datos["species"]["url"]
        datos_especies = requests.get(especies_url, timeout=20).json()
        cadena_de_evolucion_url = datos_especies["evolution_chain"]["url"]
        datos_evolucion = requests.get(
            cadena_de_evolucion_url, timeout=20).json()

        # Recorrer cadena de evoluciones en orden
        def recorrer_evoluciones(cadena):
            """Funcion que obtiene los nombres de las evoluciones de un pokemon"""
            nombres = [cadena["species"]["name"].capitalize()]
            while cadena["evolves_to"]:
                cadena = cadena["evolves_to"][0]
                nombres.append(cadena["species"]["name"].capitalize())
            return nombres

        evoluciones = recorrer_evoluciones(datos_evolucion["chain"])
        cadena_evoluciones = " -> ".join(evoluciones)

        # Mostrar resultados
        print(f"Nombre: {nombre}")
        print(f"ID: {id_pokemon}")
        print(f"Peso: {peso}")
        print(f"Altura: {altura}")
        print(f"Tipo(s): {', '.join(tipos)}")
        print(f"Cadena de evoluciones: {cadena_evoluciones}")
        print(f"Juegos en los que aparece: {', '.join(juegos)}")

    except requests.exceptions.HTTPError:
        print("Pokemon no encontrado. Verifica el nombre o numero.")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexion: {e}")
    except (ValueError, KeyError, TypeError) as e:
        print(f"Ocurrio un error inesperado: {e}")


if __name__ == "__main__":
    print("\n-------------------------------------------\n")
    solicitar_pokemon = input("Ingrese el nobmre o numero del pokemon: ")
    print("\n-------------------------------------------\n")
    obtener_pokemon(solicitar_pokemon)
# -----------------------------------------------------------------------------------
