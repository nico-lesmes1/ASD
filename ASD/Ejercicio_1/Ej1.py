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
