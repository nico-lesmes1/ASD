```
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = tokens[0] if tokens else None
    
    def advance(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None
    
    def match(self, expected):
        if self.current_token == expected:
            self.advance()
            return True
        return False
    
    def parse_S(self):
        if self.current_token in ['dos', 'cuatro', 'tres', 'uno', '$']:
            self.parse_A()
            self.parse_B()
            self.parse_C()
            self.parse_S_prime()
        else:
            raise SyntaxError(f"Error en S: token inesperado {self.current_token}")
    
    def parse_S_prime(self):
        if self.current_token == 'uno':
            self.match('uno')
            self.parse_S_prime()
        elif self.current_token == '$':
            pass
        else:
            raise SyntaxError(f"Error en S': token inesperado {self.current_token}")
    
    def parse_A(self):
        if self.current_token == 'dos':
            self.match('dos')
            self.parse_B()
            self.parse_C()
        elif self.current_token in ['cuatro', 'tres', 'uno', '$']:
            pass
        else:
            raise SyntaxError(f"Error en A: token inesperado {self.current_token}")
    
    def parse_B(self):
        if self.current_token in ['cuatro', 'tres']:
            self.parse_C()
            self.match('tres')
        elif self.current_token in ['cuatro', 'tres', 'uno', '$']:
            pass
        else:
            raise SyntaxError(f"Error en B: token inesperado {self.current_token}")
    
    def parse_C(self):
        if self.current_token == 'cuatro':
            self.match('cuatro')
            self.parse_B()
        elif self.current_token in ['cuatro', 'tres', 'uno', '$']:
            pass
        else:
            raise SyntaxError(f"Error en C: token inesperado {self.current_token}")
    
    def parse(self):
        self.parse_S()
        if self.current_token != '$':
            raise SyntaxError("Entrada no completamente consumida")
if __name__ == "__main__":
    tokens = ['dos', 'tres']

    
    try:
        parser = Parser(tokens)
        parser.parse()
        print(f"Cadena valida")
    except SyntaxError as e:
        print(f"ERROR SINTÁCTICO: {e}")
    except Exception as e:
        print(f" ERROR: {e}")
```
