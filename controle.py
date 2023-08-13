from PyQt5 import  uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "root",
    database = "cadastro_produto"
)

def funcao_principal():
    codigo = formulario.codigo.text()
    descricao = formulario.descricao.text()
    preco = formulario.preco.text()

    categoria =""


    if formulario.informatica.isChecked():
        print("Categoria Informática Selecionada")
        categoria = "Informatica"
    elif formulario.alimentos.isChecked(): 
        print("Categoria Alimentos Selecionada")
        categoria = "Alimentos"
    else:
        formulario.eletronico.isChecked()
        print("Categoria Eletrônico Selecionada")
        categoria = "Eletrônicos"

    print("Código:", codigo)
    print("Descricao:", descricao)
    print("Preco", preco)

    cursor =  banco.cursor()
    comando_SQL = "INSERT INTO produto (codigo, descricao, preco,categoria) VALUES (%s,%s,%s,%s)"
    dados= (str(codigo), str(descricao), str(preco), categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()

    formulario.codigo.setText("")
    formulario.descricao.setText("")
    formulario.preco.setText("")
    categoria =""

def funcao_ListarDados():
    TelaListarDados.show()

    cursor =  banco.cursor()
    comando_SQL = "select * from produto"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    

    TelaListarDados.tableWidget.setRowCount(len(dados_lidos))
    TelaListarDados.tableWidget.setColumnCount(5)
    
    for i in range(0, len(dados_lidos)):
        for j in range (0,5):
            TelaListarDados.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


   


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
TelaListarDados=uic.loadUi("ListarDados.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.ListarButton.clicked.connect(funcao_ListarDados)

formulario.show()
app.exec()

