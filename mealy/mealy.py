<<<<<<< HEAD
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
 
    q0.set_paths([Path("vp", q1, "0",'(Carrera|Calle)'), Path("b", q4, "0",'regex'),Path("vda", q10, "1",'dsadas'),Path("km", q8, "0",'regex')])
    q1.set_paths([Path("L", q0, "180°",'regex'), Path("D", q3, "90°",'regex')])
    q2.set_paths([Path("R", q3, "0°",'regex'), Path("U", q0, "270°",'regex')])
    q3.set_paths([Path("L", q2, "180°",'regex'), Path("U", q1, "270°",'regex')])

    q0.walk("asdadsa")
    

if __name__ == "__main__":
    test_mealy()
=======
from dataclasses import dataclass
from typing import Dict, Generic, Iterable, Iterator, Optional, Tuple, TypeVar

__all__ = ["State", "Path", "MealyResult"]


T = TypeVar("T")  
O = TypeVar("O")  


@dataclass
class Path(Generic[T, O]): 
    step: T
    dest: "State"
    value: O


@dataclass
class MealyResult(Generic[T, O]):  
    step: T
    state: "State"
    out: O

    def __str__(self) -> str:
        return f"{self.step} => {self.state} / {self.out}"


class State:
    def __init__(self, name: str, paths: Optional[Iterable[Path]] = None) -> None:
        PathDict = Dict[T, Tuple[State, O]]  
        self.name = name
        self.paths: PathDict = {}
        if paths:
            self.set_paths(paths)

    def set_path(self, path: Path) -> None:
        self.paths[path.step] = (path.dest, path.value)

    def set_paths(self, paths: Iterable[Path]) -> None:
        for path in paths:
            self.set_path(path)

    def step(self, step: T) -> Optional[MealyResult]:
        result = None
        try:
            state, out = self.paths[step]
            result = MealyResult(step, state, out)
        except KeyError:
            result = None
        return result

    def walk(self, steps: Iterable[T]) -> Iterator[MealyResult]:
        state = self
        

    def __str__(self) -> str:
        return self.name
>>>>>>> 0652fec145563b7f43db2c1571d72838f9b05299
