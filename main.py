
import random


# PARTE 1: CLASE PRINCIPAL
class Tragamonedas:

    def __init__(self, nombre, creditos):
        if creditos < 0:
            raise ValueError("Los créditos no pueden ser negativos.")

        self.nombre = nombre
        self._creditos = creditos
        self._total_apostado = 0
        self._total_premios = 0
        self._jugadas = 0
        self.simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]

    @property
    def creditos(self):
        return self._creditos

    def mostrar(self):
        if self.creditos > 0:
            estado = f"S/ {self.creditos}"
        else:
            estado = "SIN CRÉDITOS"

        print(f"🎰 {self.nombre} — Créditos: {estado}")

    # PARTE 2: GIROS ALEATORIOS
    def girar(self):
        resultado = random.choices(self.simbolos, k=3)
        print("[ " + "  ".join(resultado) + " ]")
        return resultado

    def multiplicador_jackpot(self):
        return 10

    # PARTE 3: APUESTAS Y PREMIOS
    def jugar(self, apuesta):
        if not isinstance(apuesta, int) or apuesta <= 0:
            print("⚠️ La apuesta debe ser un entero positivo.")
            return

        if apuesta > self._creditos:
            print("⚠️ No tienes créditos suficientes.")
            return

        self._creditos -= apuesta
        self._total_apostado += apuesta
        self._jugadas += 1

        resultado = self.girar()

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * self.multiplicador_jackpot()
            print(f"🏆 ¡JACKPOT! Ganaste S/ {premio}")

        elif len(set(resultado)) == 2:
            premio = apuesta * 2
            print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")

        else:
            premio = 0
            print(f"😢 Perdiste S/ {apuesta}")

        self._creditos += premio
        self._total_premios += premio

    # PARTE 5: ESTADÍSTICAS
    def mostrar_estadisticas(self):
        print(f"\n📊 {self.nombre}")
        print(f"Créditos actuales: S/ {self.creditos}")
        print(f"Jugadas realizadas: {self._jugadas}")
        print(f"Total apostado: S/ {self._total_apostado}")
        print(f"Premios entregados: S/ {self._total_premios}")
        balance = self._total_premios - self._total_apostado
        print(f"Balance del jugador: S/ {balance}")

    @property
    def estadisticas(self):
        return (
            self._jugadas,
            self._total_apostado,
            self._total_premios
        )


# PARTE 4: HERENCIA
class TragamonedasFrutas(Tragamonedas):

    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)
        self.simbolos = ["🍒", "🍋", "🍊"]


class TragamonedasClasico(Tragamonedas):

    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)
        self.simbolos = ["7️⃣", "💎", "🔔"]


class TragamonedasMundial(Tragamonedas):

    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)
        self.simbolos = ["🇵🇪", "🇦🇷", "🇫🇷", "🇧🇷"]

    def multiplicador_jackpot(self):
        return 15

    def jugar(self, apuesta):
        print("⚽ Mundial 2026: ¡Jackpot paga x15!")
        super().jugar(apuesta)


# VALIDAR ENTRADAS DEL USUARIO
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("⚠️ Ingresa un número entero válido.")
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Programa interrumpido.")
            raise SystemExit(0)


# BUCLE PARA JUGAR EN UNA MÁQUINA
def jugar_en_maquina(maquina):

    if maquina.creditos == 0:
        print(f"⚠️ {maquina.nombre} está SIN CRÉDITOS.")
        return

    print(f"\n🎰 BIENVENIDO A {maquina.nombre.upper()} 🎰")

    while maquina.creditos > 0:
        print()
        maquina.mostrar()

        apuesta = leer_entero(
            "¿Cuánto apuestas? (0 para salir): "
        )

        if apuesta == 0:
            print(
                f"💰 Saliste con S/ {maquina.creditos}. "
                "¡Vuelve pronto!"
            )
            return

        maquina.jugar(apuesta)

    print(f"⚠️ {maquina.nombre} se quedó SIN CRÉDITOS.")


# ESTADÍSTICAS DE TODAS LAS MÁQUINAS
def mostrar_estadisticas(maquinas):

    print("\n========== ESTADÍSTICAS ==========")

    for maquina in maquinas:
        maquina.mostrar_estadisticas()


# RESUMEN GENERAL DEL CASINO
def resumen_general(maquinas):

    jugadas = sum(m.estadisticas[0] for m in maquinas)
    apostado = sum(m.estadisticas[1] for m in maquinas)
    premios = sum(m.estadisticas[2] for m in maquinas)
    creditos = sum(m.creditos for m in maquinas)

    print("\n🎰 ===== RESUMEN GENERAL ===== 🎰")
    print(f"Máquinas: {len(maquinas)}")
    print(f"Jugadas realizadas: {jugadas}")
    print(f"Total apostado: S/ {apostado}")
    print(f"Premios entregados: S/ {premios}")
    print(f"Balance del casino: S/ {apostado - premios}")
    print(f"Créditos restantes: S/ {creditos}")
    print("👋 ¡Gracias por visitar CASINO ROYALE!")


# MENÚ PRINCIPAL
def main():

    maquinas = [
        TragamonedasFrutas("La Frutal", 200),
        TragamonedasClasico("La Clásica", 300),
        TragamonedasMundial("Mundial 2026", 150)
    ]

    while True:

        print("\n🎰 ===== CASINO ROYALE ===== 🎰")

        for numero, maquina in enumerate(maquinas, start=1):

            if maquina.creditos > 0:
                estado = f"S/ {maquina.creditos}"
            else:
                estado = "SIN CRÉDITOS"

            print(f"{numero}. {maquina.nombre} ({estado})")

        print("4. 📊 Mostrar estadísticas de todas")
        print("5. 🚪 Salir")

        opcion = leer_entero("\nElige una opción (1-5): ")

        if opcion in (1, 2, 3):
            jugar_en_maquina(maquinas[opcion - 1])

        elif opcion == 4:
            mostrar_estadisticas(maquinas)

        elif opcion == 5:
            resumen_general(maquinas)
            break

        else:
            print("⚠️ Opción inválida. Elige del 1 al 5.")


# INICIAR PROGRAMA
if __name__ == "__main__":
    main()
