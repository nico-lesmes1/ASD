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
        if self.current_token in ['cuatro', 'cinco', 'uno', 'dos', 'tres']:
            # S → B uno
            self.parse_B()
            self.match('uno')
        elif self.current_token == 'dos':
            # S → dos C
            self.match('dos')
            self.parse_C()
        elif self.current_token in ['$', 'tres']:
            # S → ε
            pass
        else:
            raise SyntaxError(f"Error en S: token inesperado {self.current_token}")
    
    def parse_A(self):
        if self.current_token in ['cuatro', 'cinco', 'uno', 'dos', 'tres']:
            # A → S tres B C
            self.parse_S()
            self.match('tres')
            self.parse_B()
            self.parse_C()
        elif self.current_token == 'cuatro':
            # A → cuatro
            self.match('cuatro')
        elif self.current_token == 'cinco':
            # A → ε
            pass
        else:
            raise SyntaxError(f"Error en A: token inesperado {self.current_token}")
    
    def parse_B(self):
        if self.current_token in ['cuatro', 'cinco', 'uno', 'dos', 'tres']:
            # B → A cinco C seis
            self.parse_A()
            self.match('cinco')
            self.parse_C()
            self.match('seis')
        elif self.current_token in ['uno', 'siete', 'cinco', '$', 'tres', 'seis']:
            # B → ε
            pass
        else:
            raise SyntaxError(f"Error en B: token inesperado {self.current_token}")
    
    def parse_C(self):
        if self.current_token == 'siete':
            # C → siete B
            self.match('siete')
            self.parse_B()
        elif self.current_token in ['$', 'tres', 'cinco', 'seis']:
            # C → ε
            pass
        else:
            raise SyntaxError(f"Error en C: token inesperado {self.current_token}")
    
    def parse(self):
        self.parse_S()
        if self.current_token != '$':
            raise SyntaxError("Entrada no completamente consumida")

