from validate_docbr import CPF
class CpfCnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!!")

    def cpf_e_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError ("Quantidade de dígitos inválida!!!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    def __str__(self):
        return self.format_cpf()



