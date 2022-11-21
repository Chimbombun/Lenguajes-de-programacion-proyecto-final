import nltk

class Sintaxis:
  def __init__(self):
    self._Sintaxis = """
    O -> SN SV
    SN -> Determinante Nucleo | Determinante Nucleo Adjetivo | Determinante Adjetivo Nucleo | NProp | SN SP
    SV -> Verbo | Verbo SN | Verbo SP | Verbo SN SP
    SP -> Preposicion SN
    Determinante -> 'el' | 'la' | 'un' | 'una' 
    Nucleo -> 'niño' | 'niña' | 'manzana' | 'pera' | 'cuchillo'
    NProp -> 'Juan' | 'Ana' | 'Perico' 
    Adjetivo -> 'bonito' | 'pequeña' | 'verde'
    Verbo -> 'come' | 'salta' | 'pela' | 'persigue' | 'corre'
    Preposicion -> 'de' | 'con' | 'desde' | 'a'
    Conjuncion -> 'y' | 'pero'
    """

    self._gramatica = nltk.CFG.fromstring(self._Sintaxis)
    self._analizador = nltk.ChartParser(self._gramatica)


  def verificar (self, oraciones):
    for oracion in oraciones:
      error = True
      for tree in self._analizador.parse(oracion.split()):
        error = False
      if error:
          return "Oracion sintacticamente incorrecta"
          break
    if not error:
      return "Oracion sintacticamente correcta"


      





