from python.conexao import criar_conexao, fexar_conexão

def listaPizzas():
    con = criar_conexao()
    cursor = con.cursor()
    sql = "select * from pizzas"
    cursor.execute(sql)
    pizzas = cursor.fetchall()
    fexar_conexão(con)
    return pizzas