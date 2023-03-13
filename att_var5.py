# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:54:01 2023

@author: fernando.cruz7
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:35:38 2023

@author: fernando.cruz7
"""

while True:
    try:
        nome = input("Digite o nome do Aluno: ")
        sobrenome = input("Digite o sobrenome do Aluno: ")
        portugues = float(input("Digite a nota de Português: "))
        matematica = float(input("Digite a nota de Matemática: "))
        historia = float(input("Digite a nota de História: "))
        geografia = float(input("Digite a nota de Geografia: "))
        educacao_fisica = float(input("Digite a nota de Educação Física: "))
    except Exception:
        print("\n\nUm dos valores é inválido!\n\n")
        continue
    is_correct = input("As informações estão corretas? Digite \"sim\" para continuar: ").lower()
    if is_correct in ("yes", "y", "sim", "s"):
        media = (portugues + matematica + historia + educacao_fisica + geografia) / 5
        print("\n\n")
        print(f"Nome: {nome}")
        print(f"Sobrenome: {sobrenome}")
        print(f"Nota de Português: {portugues}")
        print(f"Nota de Matemática: {matematica}")
        print(f"Nota de História: {historia}")
        print(f"Nota de Geografia: {geografia}")
        print(f"Nota de Educação Física: {educacao_fisica}")
        print(f"\n\nMedia do Aluno \"{nome} {sobrenome}\" : {media}")
        if media >= 5.0:
            print(f"\nAluno \"{nome} {sobrenome}\" foi APROVADO")
        else:
            print(f"\nAluno \"{nome} {sobrenome}\" foi REPROVADO")
        break
    else:
        continue

