from dataclasses import dataclass
from typing import Dict, Generic, Iterable, Iterator, Optional, Tuple, TypeVar
import re

__all__ = ["State", "Path", "MealyResult"]


T = TypeVar("T")  
O = TypeVar("O")  
E = TypeVar("E")
W = TypeVar("W")

@dataclass
class Path(Generic[T,O,E]): 
    step: T
    dest: "State"
    value: O
    regex: E

@dataclass
class MealyResult(Generic[T, O,W]):  
    step: T
    state: "State"
    out: O
    error:W

    def __str__(self) -> str:
        return f"{self.step} => {self.state} / {self.out} /{self.error}"


class State:
    def __init__(self, name: str, paths: Optional[Iterable[Path]] = None) -> None:
        PathDict = Dict[T, Tuple[State, O]]
        self.name = name
        self.paths: PathDict = {}
        if paths:
            self.set_paths(paths)

    def set_path(self, path: Path) -> None:
        self.paths[path.step] = {"value":(path.dest, path.value),"regex":path.regex}

    def set_paths(self, paths: Iterable[Path]) -> None:
        for path in paths:
            self.set_path(path)

    def step(self, step: T) -> Optional[MealyResult]:
        error = False
        result = None
        for paths in self.paths:
            regex = self.paths[paths]["regex"]
            state, out = self.paths[paths]["value"]
            validate = re.match(regex,step)
            if validate:
                return MealyResult(step, state, out,error)
            elif paths == "b" or paths == "r2":
                error = True
                return MealyResult(step, state, out,error)
        return result

        # TODO
        # para poder hacer la validacion de barrio manzana etc, se devera retornar el error en true a si mismo si retorna true 
        # y el estado se encuentra en algun nombre de barrio manzana etc. devera pasar al siguiente estado ya que no encontro ninguna llave para nombrar
        # try:
        #     state, out = self.paths[step]
        #     result = MealyResult(step, state, out)
        # except KeyError:
        #     result = None
        # return result

    def walk(self, steps: str) -> Iterator[MealyResult]:
        state = self
        words = re.split(r"[- #]",steps)
        
        words = list(filter(None, words))
        print(words)
        for word in words:

            print(word)
            result: Optional[MealyResult] = state.step(word)

            if result:
                if result.error:
                    print("error")
                else:
                    state = result.state
                    print(result)
            else:
                return print("invalido")

      
        """
        for step in steps:
            result: Optional[MealyResult] = state.step(step)
            if result:
                state = result.state
                yield result
            else:
                raise ValueError(
                    f"Can't take given steps. State {state.name} hasn't set a Path for Step {step}."
                )

        """
    def __str__(self) -> str:
        return self.name


def test_mealy():

    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")
    q3 = State("q3")
    q4 = State("q4")
    q5 = State("q5")
    q6 = State("q6")
    q7 = State("q7")
    q8 = State("q8")
    q9 = State("q9")
    q10 = State("q10")
    q11 = State("q11")
    q12 = State("q12")
    q13 = State("q13")
    q14 = State("q14")
    q15 = State("q15")
    q16 = State("q16")
    q17 = State("q17")
    q18 = State("q18")
    q19 = State("q19")
    q20 = State("q20")
    q21 = State("q21")
    q22 = State("q22")
    q23 = State("q23")
    q24 = State("q24")
    q25 = State("q25")
    q26 = State("q26")
    q27 = State("q27")
    q28 = State("q28")
    q29 = State("q29")
    q30 = State("q30")
    q31 = State("q31")
    q32 = State("q32")
    q33 = State("q33")
    q34 = State("q34")
    q35 = State("q35")
    
 
    q0.set_paths([Path("tv", q1, "0",r'\b(Autopista|Avenida|Avenida Calle|Avenida Carrera|Bulevar|Calle|Carrera|Carretera|Circular|Circunvalar|Cuentas Corridas|Diagonal|Pasaje|Paseo|Peatonal|Transversal|Variante|Via|Troncal)\b'), Path("br2", q19, "0",r'\b(Barrio|Ciudadela|Supermanzana)\b'),Path("vda", q27, "0",r'\bVereda\b'),Path("km", q31, "0",r'\bKilometro\b')])
    #Urbana
    q1.set_paths([Path("nv", q2, "0",r'^[1-9][0-9]{0,2}(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q2.set_paths([Path("bis", q3, "0",r'^BIS$'),Path("c", q5, "0",r'^(NORTE|SUR|ESTE|OESTE)$'),Path("nv", q6, "0",r'^[1-9][0-9]{0,2}(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q3.set_paths([Path("lp", q4, "0",r'^(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$'),Path("nv", q6, "0",r'^[1-9][0-9]{0,2}(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q4.set_paths([Path("c", q5, "0",r'^(NORTE|SUR|ESTE|OESTE)$'),Path("nv", q6, "0",r'^[1-9][0-9]{0,2}(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q5.set_paths([Path("nv", q6, "0",r'^[1-9][0-9]{0,2}(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q6.set_paths([Path("bis", q7, "0",r'^BIS$'),Path("np", q9, "1",r'\b[1-9][0-9]{0,2}\b')])
    q7.set_paths([Path("lp", q8, "0",r'^(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$'),Path("np", q9, "1",r'\b[1-9][0-9]{0,2}\b')])
    q8.set_paths([Path("np", q9, "1",r'\b[1-9][0-9]{0,2}\b')])
    q9.set_paths([Path("c", q10, "1",r'^(NORTE|SUR|ESTE|OESTE)$'),Path("br", q11, "0",r'^(Barrio|Ciudadela|Supermanzana)$'),Path("u", q13, "0",r'^(Bloque|Celula|conjunto Residencial|Etapa|Urbanizacion|Sector|Torre|Zona)$'),Path("ma", q15, "0",r'^(Manzana|Interior|Sector|Etapa|Edificio|Modulo|Torre)$'),Path("tp", q17, "0",r'^(Altillo|Apartamento|Bodega|Casa|Consultorio|Deposito|Garaje|Local|Lote|Mezzanine|Oficina|Parqueadero|Pent-House|Planta|Predio|Semisotano|Sotano|Suite|Terraza|Unidad)$')])
    q10.set_paths([Path("br", q11, "0",r'^(Barrio|Ciudadela|Supermanzana)$'),Path("u", q13, "0",r'^(Bloque|Celula|conjunto Residencial|Etapa|Urbanizacion|Sector|Torre|Zona)$'),Path("ma", q15, "0",r'^(Manzana|Interior|Sector|Etapa|Edificio|Modulo|Torre)$'),Path("tp", q17, "0",r'^(Altillo|Apartamento|Bodega|Casa|Consultorio|Deposito|Garaje|Local|Lote|Mezzanine|Oficina|Parqueadero|Pent-House|Planta|Predio|Semisotano|Sotano|Suite|Terraza|Unidad)$')])
    q11.set_paths([Path("nb", q12, "1",r'^\w+$')])
    q12.set_paths([Path("u", q13, "0",r'^(Bloque|Celula|conjunto Residencial|Etapa|Urbanizacion|Sector|Torre|Zona)$'),Path("ma", q15, "0",r'^(Manzana|Interior|Sector|Etapa|Edificio|Modulo|Torre)$'),Path("tp", q17, "0",r'^(Altillo|Apartamento|Bodega|Casa|Consultorio|Deposito|Garaje|Local|Lote|Mezzanine|Oficina|Parqueadero|Pent-House|Planta|Predio|Semisotano|Sotano|Suite|Terraza|Unidad)$')])
    q13.set_paths([Path("nu", q14, "1",r'^\w+$')])
    q14.set_paths([Path("ma", q15, "0",r'^(Manzana|Interior|Sector|Etapa|Edificio|Modulo|Torre)$'),Path("tp", q17, "0",r'^(Altillo|Apartamento|Bodega|Casa|Consultorio|Deposito|Garaje|Local|Lote|Mezzanine|Oficina|Parqueadero|Pent-House|Planta|Predio|Semisotano|Sotano|Suite|Terraza|Unidad)$')])
    q15.set_paths([Path("nma", q16, "1",r'^\w+$')])
    q16.set_paths([Path("tp", q17, "0",r'^(Altillo|Apartamento|Bodega|Casa|Consultorio|Deposito|Garaje|Local|Lote|Mezzanine|Oficina|Parqueadero|Pent-House|Planta|Predio|Semisotano|Sotano|Suite|Terraza|Unidad)$')])
    q17.set_paths([Path("ip", q18, "1",r'^\w+$')])
    
    #Barrio // urbana
    q19.set_paths([Path("nb", q20, "0",r'^\w+$')])
    q20.set_paths([Path("u", q21, "0",r'^(Bloque|Celula|conjunto Residencial|Etapa|Urbanizacion|Sector|Torre|Zona)$')])
    q21.set_paths([Path("nu", q22, "0",r'^\w+$')])
    q22.set_paths([Path("ma", q23, "0",r'^(Manzana|Interior|Sector|Etapa|Edificio|Modulo|Torre)$')])
    q23.set_paths([Path("nma", q24, "1",r'^\w+$')])
    q24.set_paths([Path("tp", q25, "0",r'^(Altillo|Apartamento|Bodega|Casa|Consultorio|Deposito|Garaje|Local|Lote|Mezzanine|Oficina|Parqueadero|Pent-House|Planta|Predio|Semisotano|Sotano|Suite|Terraza|Unidad)$')])
    q25.set_paths([Path("ip", q26, "1",r'^\w+$')])
    
    #Vereda // rural
    q27.set_paths([Path("nvda", q28, "1",r'^\w+$')])
    q28.set_paths([Path("sc", q29, "0",r'^Sector$')])
    q29.set_paths([Path("nsc", q30, "1",r'^\w+$')])
    #Km y via //rural
    q31.set_paths([Path("nmk", q32, "0",r'^[1-9][0-9]{0,2}$')])
    q32.set_paths([Path("v", q33, "0",r'^Via$')])
    q33.set_paths([Path("n1", q34, "1",r'^\w+$')])
    q34.set_paths([Path("n2", q35, "1",r'^\w+$')])
    
    q0.walk("Carrera 7 BIS B #1 BIS-20 Apartamento 201")
    # q0.walk("Vereda San_Juan Sector La_uida")
    # q0.walk("Barrio San_Juan Etapa 3 Manzana 4 Apartamento 501")
    # q0.walk("Kilometro 32 Via Duitama-Paipa")
    

if __name__ == "__main__":
    test_mealy()
