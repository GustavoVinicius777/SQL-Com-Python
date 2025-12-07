class Cliente:
    def __init__(self, id=None, nome='', email='', telefone='', data_criacao=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data_criacao = data_criacao

    def __repr__(self):
        return f"Cliente(id={self.id}, nome='{self.nome}', email='{self.email}', telefone='{self.telefone}', data_criacao='{self.data_criacao}')"
