#
# tmdb15k/genres.py
#

class Genre:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Genre({self.id}, {self.name})"

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

def from_str(v: str) -> Genre:
    return Genre(hash(v), v)

def from_json(v: dict | str | None) -> Genre | None:
    if v is None:
        return None

    if isinstance(v, str):
        return from_str(v)

    return Genre(v["id"], v["name"])
