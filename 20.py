class ValorDAAC:
    def __init__(self, valor_DAAC):
        self.valor_DAAC = valor_DAAC

    def __add__(self, otro_DAAC):
        if isinstance(otro_DAAC, ValorDAAC):
            return ValorDAAC(self.valor_DAAC + otro_DAAC.valor_DAAC)
        return ValorDAAC(self.valor_DAAC + otro_DAAC)

    def __sub__(self, otro_DAAC):
        if isinstance(otro_DAAC, ValorDAAC):
            return ValorDAAC(self.valor_DAAC - otro_DAAC.valor_DAAC)
        return ValorDAAC(self.valor_DAAC - otro_DAAC)

    def __mul__(self, otro_DAAC):
        if isinstance(otro_DAAC, ValorDAAC):
            return ValorDAAC(self.valor_DAAC * otro_DAAC.valor_DAAC)
        return ValorDAAC(self.valor_DAAC * otro_DAAC)

    def __eq__(self, otro_DAAC):
        if isinstance(otro_DAAC, ValorDAAC):
            return self.valor_DAAC == otro_DAAC.valor_DAAC
        return self.valor_DAAC == otro_DAAC

    def __lt__(self, otro_DAAC):
        if isinstance(otro_DAAC, ValorDAAC):
            return self.valor_DAAC < otro_DAAC.valor_DAAC
        return self.valor_DAAC < otro_DAAC

    def __gt__(self, otro_DAAC):
        if isinstance(otro_DAAC, ValorDAAC):
            return self.valor_DAAC > otro_DAAC.valor_DAAC
        return self.valor_DAAC > otro_DAAC

    def __contains__(self, item_DAAC):
        return str(item_DAAC) in str(self.valor_DAAC)

    def __call__(self, extra_DAAC=0):
        return self.valor_DAAC + extra_DAAC

    def __str__(self):
        return f"ValorDAAC({self.valor_DAAC})"


if __name__ == "__main__":
    a_DAAC = ValorDAAC(10)
    b_DAAC = ValorDAAC(4)

    print(a_DAAC + b_DAAC)
    print(a_DAAC - 2)
    print(a_DAAC * b_DAAC)

    print(a_DAAC == 10)
    print(a_DAAC > b_DAAC)
    print(a_DAAC < 20)

    print("10" in a_DAAC)
    print(a_DAAC(5))
