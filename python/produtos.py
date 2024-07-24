from python.conexao import criar_conexao, fexar_conexão

def listaPizzas():
    con = criar_conexao()
    cursor = con.cursor()
    sql = "select * from pizzas"
    cursor.execute(sql)
    pizzas = cursor.fetchall()
    fexar_conexão(con)
    return pizzas


def listaMiniPizza():
    con = criar_conexao()
    cursor = con.cursor()
    sql = "select * from miniPizza"
    cursor.execute(sql)
    miniPizza = cursor.fetchall()
    fexar_conexão(con)
    return miniPizza

def listaBebidas():
    con = criar_conexao()
    cursor = con.cursor()
    sql = "select * from bebidas"
    cursor.execute(sql)
    bebidas = cursor.fetchall()
    fexar_conexão(con)
    return bebidas