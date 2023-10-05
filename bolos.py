class Roll:
    def __init__(self):
        self.pines: int = 10


class Frame:
    puntaje_Local_Temporal: int = 0
    """Este puntaje cumplira la funcion de llevar un conteo externo, entre los frames futuros para obtener los 
    que faltan para calcular correctamente el puntaje de este frame"""

    def __init__(self):
        self.puntaje: int = 0
        self.roles: int = 0

    def spare(self, resultado) -> bool:
        if resultado == 10 - self.puntaje:  # SI el nuevo numero derribado es 10, al ser su segundo intento, entonces...
            return True
        else:
            return False

    def strike(self, resultado) -> bool:
        if resultado == 10:
            return True
        else:
            return False

    def jugar_roll(self, derribos: int = 0) -> int:
        if self.roles == 0:
            if self.strike(derribos):
                self.puntaje = 10
                Frame.puntaje_Local_Temporal += self.puntaje
                """si es strike, el puntaje del primer roll es 10, es fijo que minimo sera este,
                   pero aun no se puede calcular hasta no hacer dos jugadas de los siguientes dos frames """
                return 0

            else:
                self.puntaje = derribos
        elif self.roles == 1:
            if self.spare(derribos):
                return 1
            else:
                self.puntaje += derribos

        self.roles += 1


class Game(Frame):

    def __init__(self):
        super().__init__()
        self.general_score: int = 0
        self.numero_frames: int = 9

    def bucle_inicial(self):
        derribos: int

        def jugar_frame(self, derribos=None):

            """Retorna un numero el cual es una clave valor, para determinar que funcion se debe seguir, si llamar mas frames
            """

            """Si retorna 1 significa que los siguientes dos frames determinan el valor de este."""
            """ Aunque ya se actualizo la parte general"""
            if super().jugar_roll(derribos) == 0:
                for _ in range(3):
                    self.general_score += Frame.puntaje_Local_Temporal
                    Frame.puntaje_Local_Temporal = 0
                    if self.numero_frames-1 != 0:
                        self.bucle_inicial()
                        self.numero_frames -= 1
                        return self.general_score
            elif super().jugar_roll(derribos) == 1:
                for _ in range(2):
                    self.general_score += Frame.puntaje_Local_Temporal
                    Frame.puntaje_Local_Temporal = 0
                    self.bucle_inicial()

            elif super().jugar_roll(derribos) == 2:
                pass

        jugar_frame(derribos)
