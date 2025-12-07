from database import get_connection
from models import Cliente

class ClienteDAO:

    def salvar(self, cliente: Cliente):
        conn = get_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
        cursor.execute(sql, (cliente.nome, cliente.email, cliente.telefone))
        conn.commit()

        cliente.id = cursor.lastrowid

        cursor.close()
        conn.close()

    def atualizar(self, cliente: Cliente):
        conn = get_connection()
        cursor = conn.cursor()

        sql = "UPDATE clientes SET nome=%s, email=%s, telefone=%s WHERE id=%s"
        cursor.execute(sql, (cliente.nome, cliente.email, cliente.telefone, cliente.id))
        conn.commit()

        cursor.close()
        conn.close()

    def deletar(self, id: int):
        conn = get_connection()
        cursor = conn.cursor()

        sql = "DELETE FROM clientes WHERE id=%s"
        cursor.execute(sql, (id,))
        conn.commit()

        cursor.close()
        conn.close()

    def buscar_por_id(self, id: int):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = "SELECT * FROM clientes WHERE id=%s"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row:
            return Cliente(**row)
        return None

    def listar_todos(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = "SELECT * FROM clientes ORDER BY id"
        cursor.execute(sql)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return [Cliente(**row) for row in rows]
