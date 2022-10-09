from dataclasses import dataclass
from distutils.log import error
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
        # para poder hacer la validacion de barrio manzana etc, se devera retornal el error en true a si mismo si retorna true 
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
 
        result: Optional[MealyResult] = state.step(words[0])

        if result:
            if result.error:
                print("error")
            else:
                print(result)
        else:
            print("mas error")
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
    
 
    q0.set_paths([Path("tv", q1, "0",'(Carrera|Calle)'), Path("br2", q30, "0",'regex'),Path("vda", q25, "0",'regex'),Path("km", q21, "0",'regex')])
    #Urbana
    q1.set_paths([Path("nv", q2, "0",'regex')])
    q2.set_paths([Path("lv", q3, "0",'regex')])
    q3.set_paths([Path("bis", q4, "0",'regex')])
    q4.set_paths([Path("lp", q5, "0",'regex')])
    q5.set_paths([Path("c", q6, "0",'regex')])
    q6.set_paths([Path("nv", q7, "0",'regex')])
    q7.set_paths([Path("lv", q8, "0",'regex')])
    q8.set_paths([Path("bis", q9, "0",'regex')])
    q9.set_paths([Path("ls", q10, "0",'regex')])
    q10.set_paths([Path("np", q11, "1",'regex')])
    q11.set_paths([Path("c", q20, "1",'regex')])
    q20.set_paths([Path("br", q12, "0",'regex')])
    q12.set_paths([Path("nb", q13, "1",'regex')])
    q13.set_paths([Path("u", q14, "0",'regex')])
    q14.set_paths([Path("nu", q15, "1",'regex')])
    q15.set_paths([Path("ma", q16, "0",'regex')])
    q16.set_paths([Path("nma", q17, "1",'regex')])
    q17.set_paths([Path("tp", q18, "0",'regex')])
    q18.set_paths([Path("ip", q19, "1",'regex')])
    #Km y via //rural
    q21.set_paths([Path("nkm", q22, "0",'regex')])
    q22.set_paths([Path("v", q23, "0",'regex')])
    q23.set_paths([Path("n1", q24, "1",'regex')])
    q24.set_paths([Path("n2", q29, "1",'regex')])
    #Barrio // urbana
    q30.set_paths([Path("nb2", q31, "0",'regex')])
    q31.set_paths([Path("u2", q32, "0",'regex')])
    q32.set_paths([Path("nu2", q33, "0",'regex')])
    q33.set_paths([Path("ma2", q34, "0",'regex')])
    q34.set_paths([Path("nma2", q35, "0",'regex')])
    q35.set_paths([Path("tp", q36, "0",'regex')])
    q36.set_paths([Path("ip", q37, "1",'regex')])
    #Vereda // rural
    q25.set_paths([Path("nvda", q26, "1",'regex')])
    q26.set_paths([Path("sc", q27, "0",'regex')])
    q27.set_paths([Path("nsc", q28, "1",'regex')])
    
   
    q0.walk("test")
    

if __name__ == "__main__":
    test_mealy()
