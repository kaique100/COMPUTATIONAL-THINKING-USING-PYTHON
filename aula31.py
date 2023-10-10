import cx_Oracle
import json

print("lendo arquivo com senhas...")
path = r"D:\COMPUTATIONAL-THINKING-USING-PYTHON\login.json"

with open(path, 'r') as arquivo:
    dados = json.load(arquivo)
login=dados["user"]
senha=dados["password"]
print("senha recuperada!")

print("Apontando biblioteca Oracle")
cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\logonrmlocal\Downloads\instantclient-basic-windows.x64-21.11.0.0.0dbru\instantclient_21_11")
print("feito\n")


print("Criando dsn\n")
dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521,sid='ORCL')
print("dsn feito\n")

print("abrindo conexao\n")
conn = cx_Oracle.connect(user=login,password=senha, dsn=dsn)
print("conexao estabelecida\n")


print("Criando Cursor\n")
cursor = conn.cursor()
print("cursor criado\n")



# print("Criando uma entrada no banco\n")
# cursor.execute("insert into TB_USUARIO (ID,NOME) VALUES(:valor1, :valor2)", valor1=1,valor2="Kaique")
# conn.commit()
# print("entrada registrada\n")

cursor.execute("select * from TB_USUARIO")
linhas = cursor.fetchall()

print(linhas)

for i in linhas:
    print(i)




cursor.execute("insert into TB_USUARIO (ID,NOME) VALUES(:valor1, :valor2)", valor1=1,valor2="Kaique")
conn.commit()


print("encerrando Cursor\n")
cursor.close()
print("Conexao Cursor\n")


print("encerrando conexao\n")
conn.close()
print("Conexao encerrada\n")