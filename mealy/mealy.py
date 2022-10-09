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
        words = re.split(" ",steps)
 
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
                return print("mas error")

      
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
    q36 = State("q36")
    q37 = State("q37")
    
 
    q0.set_paths([Path("tv", q1, "0",r'\b(AU|AV|AC|AK|BL|CL|KR|CT|CQ|CV|CC|DG|PJ|PS|PT|TV|VT|VI)\b'), Path("br2", q30, "0",r'\b(BR|CD|SM)\b'),Path("vda", q25, "0",r'\bVDA\b'),Path("km", q21, "0",r'\bKM\b')])
    #Urbana
    q1.set_paths([Path("nv", q2, "0",r'\b[1-9][0-9]{0,2}\b')])
    q2.set_paths([Path("lv", q3, "0",r'^(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q3.set_paths([Path("bis", q4, "0",r'^BIS$')])
    q4.set_paths([Path("lp", q5, "0",r'^(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q5.set_paths([Path("c", q6, "0",r'^(NORTE|SUR|ESTE|OESTE)$')])
    q6.set_paths([Path("nv", q7, "0",r'\b[1-9][0-9]{0,2}\b')])
    q7.set_paths([Path("lv", q8, "0",r'^(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q8.set_paths([Path("bis", q9, "0",r'^BIS$')])
    q9.set_paths([Path("ls", q10, "0",r'^(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q10.set_paths([Path("np", q11, "1",r'\b[1-9][0-9]{0,2}\b')])
    q11.set_paths([Path("c", q20, "1",r'^(NORTE|SUR|ESTE|OESTE)$')])
    q20.set_paths([Path("br", q12, "0",r'^(BR|CD|SM)$')])
    q12.set_paths([Path("nb", q13, "1",r'^\w+$')])
    q13.set_paths([Path("u", q14, "0",r'^(BQ|CU|CO|ET|UR|SC|TO|ZN)$')])
    q14.set_paths([Path("nu", q15, "1",r'^\w+$')])
    q15.set_paths([Path("ma", q16, "0",r'^(MZ|IN|SC|ET|ED|MD|TO)$')])
    q16.set_paths([Path("nma", q17, "1",r'^\w+$')])
    q17.set_paths([Path("tp", q18, "0",r'^(AL|AP|BG|CD|CN|DP|DS|GA|GS|LC|LM|LT|MN|OF|PA|PN|PL|PD|SS|SO|ST|TZ|UN|UL)$')])
    q18.set_paths([Path("ip", q19, "1",r'^\w+$')])
    #Km y via //rural
    q21.set_paths([Path("nkm", q22, "0",r'^[1-9][0-9]{0,1}$')])
    q22.set_paths([Path("v", q23, "0",r'^V$')])
    q23.set_paths([Path("n1", q24, "1",r'^[A-Z]+$')])
    q24.set_paths([Path("n2", q29, "1",r'^[A-Z]+$')])
    #Barrio // urbana
    q30.set_paths([Path("nb2", q31, "0",r'^\w+$')])
    q31.set_paths([Path("u2", q32, "0",r'^(BQ|CU|CO|ET|UR|SC|TO|ZN)$')])
    q32.set_paths([Path("nu2", q33, "0",r'^\w+$')])
    q33.set_paths([Path("ma2", q34, "0",r'^(MZ|IN|SC|ET|ED|MD|TO)$')])
    q34.set_paths([Path("nma2", q35, "0",r'^\w+$')])
    q35.set_paths([Path("tp", q36, "0",r'^(AL,AP,BG,CD,CN,DP,DS,GA,GS,LC,LM,LT,MN,OF,PA,PN,PL,PD,SS,SO,ST,TZ,UN,UL)$')])
    q36.set_paths([Path("ip", q37, "1",r'^\w+$')])
    #Vereda // rural
    q25.set_paths([Path("nvda", q26, "1",r'^\w+$')])
    q26.set_paths([Path("sc", q27, "0",r'^SC$')])
    q27.set_paths([Path("nsc", q28, "1",r'^\w+$')])
    
   
    q0.walk("TV 12 A BIS A NORTE 12 A BIS AB 12 NORTE BR SAN_LUCAS BQ 5 MZ 1 AP 201")
    

if __name__ == "__main__":
    test_mealy()
