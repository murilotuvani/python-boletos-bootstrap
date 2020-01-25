import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="autogeral"
)

sql = """
    select b.codigo, b.loja, b.nosso_numero, b.vencimento, b.valor
      from boletos b join cadastros_emails e on b.cadastro_codigo=e.cadastro_codigo and b.cadastro_loja=e.cadastro_loja
     where e.recebe_cobranca=1 and e.email='murilo@autogeral.com.br'
     order by b.pago, b.vencimento
     limit 20
      """

mycursor = mydb.cursor()
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  codigo = x[0]
  loja = x[1]
  nosso_numero = x[2]
  vencimento = x[3]
  valor = x[4]

  print('Vencimento : ', vencimento, ' Valor : ', valor)

myresult.clear()
mycursor.close()
mydb.close()

