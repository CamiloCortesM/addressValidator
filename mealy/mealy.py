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
