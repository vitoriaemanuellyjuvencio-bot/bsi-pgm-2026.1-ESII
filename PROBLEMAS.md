# Problemas Identificados — Leitura Inicial do Código

Este arquivo é preenchido pelos estudantes na Aula 1 após a leitura do código legado.
Descreva em linguagem livre tudo que parecer estranho, errado ou difícil de entender.
Não é necessário usar termos técnicos neste momento.

---

## Minha leitura inicial

# Problemas encontrados no sistema

1. Uso de variáveis globais  
O sistema usa listas globais de equipamentos e empréstimos. Isso é estranho porque a própria classe Sistema deveria controlar esses dados, em vez de depender de coisas fora dela.

2. Mistura de responsabilidades  
A classe Sistema faz muitas coisas ao mesmo tempo: controla empréstimos, calcula multa e ainda “envia email” (com print). Isso deixa o código confuso e difícil de organizar.

3. Cálculo de multa repetido  
A lógica de cálculo de multa aparece em mais de um lugar (na devolução e na listagem de atrasados). Isso é ruim porque, se precisar mudar a regra, tem que alterar em vários pontos.

4. Regra de multa pouco flexível  
O cálculo da multa depende de vários if/elif com o tipo do equipamento. Se for adicionado um novo tipo, será necessário modificar o código, o que não parece uma boa prática.

5. Interface misturada com a lógica  
O menu (input e print) está no mesmo arquivo que a lógica do sistema. Isso dificulta separar o funcionamento interno do sistema da forma como o usuário interage com ele.

6. Falta de validação de dados  
O sistema não valida bem os dados digitados pelo usuário. Por exemplo, se a pessoa digitar um ID inválido ou texto no lugar de número, pode dar erro.

7. “Envio de email” não é real  
O sistema mostra mensagens como se estivesse enviando email, mas na verdade só imprime no console. Isso pode confundir sobre o que o sistema realmente faz.

---

## Revisão com vocabulário técnico

*(Este espaço será preenchido após a Aula 4, quando os termos técnicos corretos forem aprendidos)*
