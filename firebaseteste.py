import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('firebase_sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL':'https://cadastrodesafioproz-default-rtdb.firebaseio.com'
})

pessoas=['pessoa1', 'pessoa2', 'pessoa3']


for i in range(len(pessoas)):
    nome =input("Digite seu nome:")
    cpf= input("Digite seu cpf:")
    rg= input("Digite seu rg:")
    data_de_nascimento=input("Digite sua data de nascimento:")
    sexo=input("Digite seu sexo:")
    signo=input("Digite seu signo:")
    mae=input("Digite o nome da sua mae:")
    pai=input("Digite o nome do seu pai:")
    email=input("Digite seu email:")
    senha=input("Digite sua senha:")
    endereco=input("Digite seu endereço:")
    cep=input("Digite seu cep:")
    numero=input("Digite seu numero:")
    bairro=input("Digite seu bairro:")
    cidade=input("Digite seu cidade:")
    estado=input("Digite seu estado:")
    telefone=input("Digite seu telefone:")
    celular=input("Digite seu celular:")
    altura=input("Digite sua altura:")
    peso=input("Digite seu peso:")
    tipo_sanguineo=input("Digite seu tipo sanguineo:")
    cor_favorita=input("Digite sua cor favorita:")
    ref = db.reference('/cadastro/%s'%pessoas[i])
    ref.set({
                'nome': nome,
                'cpf': cpf,
                'rg': rg,
                'data de nascimento': data_de_nascimento,
                'sexo':sexo ,
                'signo': signo,
                'mae': mae,
                'pai':pai ,
                'email': email,
                'senha': senha,
                'endereco':endereco ,
                'cep': cep,
                'numero': numero,
                'bairro': bairro,
                'cidade':cidade ,
                'estado': estado,
                'telefone': telefone,
                'celular':celular ,
                'altura': altura,
                'peso': peso,
                'tipo sanguineo': tipo_sanguineo,
                'cor favorita':cor_favorita ,
})
