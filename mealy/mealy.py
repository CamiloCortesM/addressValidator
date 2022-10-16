from dataclasses import dataclass
from typing import Dict, Generic, Iterable, Iterator, Optional, Tuple, TypeVar
import re

__all__ = ["State", "Path", "MealyResult"]


T = TypeVar("T")  
O = TypeVar("O")  
E = TypeVar("E")

@dataclass
class Path(Generic[T,O,E]): 
    step: T
    dest: "State"
    value: O
    regex: E

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
        self.paths[path.step] = {"value":(path.dest, path.value),"regex":path.regex}

    def set_paths(self, paths: Iterable[Path]) -> None:
        for path in paths:
            self.set_path(path)

    def step(self, step: T) -> Optional[MealyResult]:
        result = None
        for paths in self.paths:
            regex = self.paths[paths]["regex"]
            state, out = self.paths[paths]["value"]
            validate = re.match(regex,step)
            if validate:
                return MealyResult(step, state, out)
        return result

    def walk(self, steps: str) -> Iterator[MealyResult]:
        state = self
        out = None
        words = re.split(r"[- #]",steps)
        words = list(filter(None, words))
        if(words[0] == "Avenida" and words[1] == "Calle" or words[0] == "Avenida" and words[1]=="Carrera" or words[0] == "Cuentas" and words[1]=="Corridas"):
            words.insert(0,words[0]+" "+words[1])
            words.pop(1)
            words.pop(1)

        for word in words:
            result: Optional[MealyResult] = state.step(word)
            if result:
                    state = result.state
                    out = result.out
                    print(result)
            else:
                print(result)
                return False
        if out == "1":
            return True
        return False
      
    def __str__(self) -> str:
        return self.name