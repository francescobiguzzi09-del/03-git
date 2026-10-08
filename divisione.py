def divisione(a: float, b: float):
    if b == 0:
        return "Error: divisor must not be 0"
    
    divisione= a/b
    return divisione

if __name__ == "__main__":
    print(divisione(10,2))