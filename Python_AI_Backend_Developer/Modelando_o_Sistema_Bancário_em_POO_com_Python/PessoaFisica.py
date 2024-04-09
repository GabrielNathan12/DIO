from Cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self,nome, data_nasc, cpf ,endereco: str) -> None:
        super().__init__(endereco)
        self._nome = nome
        self._data_nasc = data_nasc
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    @property
    def data_nasc(self):
        return self._data_nasc
    @property
    def cpf(self):
        return self._cpf