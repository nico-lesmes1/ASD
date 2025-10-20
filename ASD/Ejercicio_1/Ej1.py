class ParserEjercicio1:
    def __init__(self, tokens):
        self.tokens = tokens + ['$']
        self.pos = 0
        self.current_token = self.tokens[0]
        self.depth = 0
    
    def log(self, message):
        indent = "  " * self.depth
        print(f"{indent}{message}")
    
    def advance(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None
    
    def match(self, expected):
        if self.current_token == expected:
            self.log(f"✓ Coincide: '{expected}'")
            self.advance()
            return True
        return False
    
    def parse_S(self):
        self.depth += 1
        self.log("Analizando S")
        
        if self.current_token in ['dos', 'cuatro', 'seis', '$']:
            # S → A B C
            self.parse_A()
            self.parse_B()
            self.parse_C()
        elif self.current_token in ['uno', 'cuatro', 'tres']:
            # S → D E
            self.parse_D()
            self.parse_E()
        else:
            raise SyntaxError(f"Error en S: token inesperado '{self.current_token}'")
        
        self.log("S analizado correctamente")
        self.depth -= 1
    
    def parse_A(self):
        self.depth += 1
        self.log("Analizando A")
        
        if self.current_token == 'dos':
            # A → dos B tres
            self.match('dos')
            self.parse_B()
            self.match('tres')
        elif self.current_token in ['cuatro', 'seis', 'tres', '$']:
            # A → ε
            self.log("ε (vacío)")
        else:
            raise SyntaxError(f"Error en A: token inesperado '{self.current_token}'")
        
        self.log("A analizado correctamente")
        self.depth -= 1
    
    def parse_B(self):
        self.depth += 1
        self.log("Analizando B")
        
        if self.current_token in ['seis', 'tres', 'cinco', '$']:
            # B → ε B'
            self.parse_B_prime()
        elif self.current_token in ['cuatro', 'seis', 'tres', 'cinco', '$']:
            # B → B'
            self.parse_B_prime()
        else:
            raise SyntaxError(f"Error en B: token inesperado '{self.current_token}'")
        
        self.log("B analizado correctamente")
        self.depth -= 1
    
    def parse_B_prime(self):
        self.depth += 1
        self.log("Analizando B'")
        
        if self.current_token == 'cuatro':
            # B' → cuatro C cinco B'
            self.match('cuatro')
            self.parse_C()
            self.match('cinco')
            self.parse_B_prime()
        elif self.current_token in ['seis', 'tres', 'cinco', '$']:
            # B' → ε
            self.log("ε (vacío)")
        else:
            raise SyntaxError(f"Error en B': token inesperado '{self.current_token}'")
        
        self.log("B' analizado correctamente")
        self.depth -= 1
    
    def parse_C(self):
        self.depth += 1
        self.log("Analizando C")
        
        if self.current_token == 'seis':
            # C → seis A B
            self.match('seis')
            self.parse_A()
            self.parse_B()
        elif self.current_token in ['cinco', '$']:
            # C → ε
            self.log("ε (vacío)")
        else:
            raise SyntaxError(f"Error en C: token inesperado '{self.current_token}'")
        
        self.log("C analizado correctamente")
        self.depth -= 1
    
    def parse_D(self):
        self.depth += 1
        self.log("Analizando D")
        
        if self.current_token == 'uno':
            # D → uno A E
            self.match('uno')
            self.parse_A()
            self.parse_E()
        elif self.current_token in ['cuatro', 'tres']:
            # D → B
            self.parse_B()
        else:
            raise SyntaxError(f"Error en D: token inesperado '{self.current_token}'")
        
        self.log("D analizado correctamente")
        self.depth -= 1
    
    def parse_E(self):
        self.depth += 1
        self.log("Analizando E")
        
        if self.current_token == 'tres':
            self.match('tres')
        else:
            raise SyntaxError(f"Error en E: token inesperado '{self.current_token}'")
        
        self.log("E analizado correctamente")
        self.depth -= 1
    
    def parse(self):
        print("=== EJERCICIO 1 - INICIANDO ANÁLISIS ===")
        print(f"Gramática: S → A B C | D E")
        print(f"Tokens: {self.tokens}")
        print()
        
        self.parse_S()
        
        if self.current_token != '$':
            raise SyntaxError(f"Entrada no completamente consumida. Token restante: '{self.current_token}'")
        
        print()
        print("=== ANÁLISIS COMPLETADO CON ÉXITO ===")
        print("✓ La cadena es sintácticamente válida para la Gramática 1")

# Pruebas para Ejercicio 1
def probar_ejercicio1():
    print("=" * 60)
    print("PRUEBAS EJERCICIO 1")
    print("=" * 60)
    
    # Prueba 1: Cadena válida
    print("\n--- Prueba 1: Cadena válida ---")
    try:
        tokens1 = ['uno', 'dos', 'tres']
        parser1 = ParserEjercicio1(tokens1)
        parser1.parse()
    except SyntaxError as e:
        print(f"❌ ERROR: {e}")
    
    # Prueba 2: Otra cadena válida
    print("\n--- Prueba 2: Otra cadena válida ---")
    try:
        tokens2 = ['dos', 'cuatro', 'cinco']
        parser2 = ParserEjercicio1(tokens2)
        parser2.parse()
    except SyntaxError as e:
        print(f"❌ ERROR: {e}")
    
    # Prueba 3: Cadena inválida
    print("\n--- Prueba 3: Cadena inválida ---")
    try:
        tokens3 = ['cinco']  # Token no permitido
        parser3 = ParserEjercicio1(tokens3)
        parser3.parse()
    except SyntaxError as e:
        print(f"❌ ERROR: {e}")