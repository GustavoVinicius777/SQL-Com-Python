from database import get_connection
from models import Cliente

class ClienteDAO:

    def salvar(self, cliente: Cliente):
        conn = get_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
        cursor.execute(sql, (cliente.nome, cliente.email, cliente.telefone))
        conn.commit()
        cursor.close()
        conn.close()

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes ORDER BY id")
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        return items

    def buscar(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes WHERE id=%s", (id,))
        item = cursor.fetchone()
        cursor.close()
        conn.close()
        return item

    def atualizar(self, cliente: Cliente):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE clientes SET nome=%s, email=%s, telefone=%s WHERE id=%s",
            (cliente.nome, cliente.email, cliente.telefone, cliente.id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def deletar(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
