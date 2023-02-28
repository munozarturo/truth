
notation: dict = {
    "logic": {
        ".": "and",
        "+": "or",
        "'": "not",
        "^": "xor",
    }
}

lgc: str = "x'.y' + x'.y + x.y' + x.y"

def parse_logic(lgc: str):
    
    for c in lgc:
        print(c)
    
    return lgc