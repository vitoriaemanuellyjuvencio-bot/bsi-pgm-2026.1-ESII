## Aula 04 — SRP

A parte mais difícil foi separar a responsabilidade de notificação da lógica de empréstimos, pois ambas acontecem no mesmo fluxo.

A dificuldade surgiu porque, ao registrar ou devolver um empréstimo, o sistema também envia uma mensagem, o que dá a impressão de que tudo deve ficar junto.

No entanto, com base no conceito de SRP apresentado por Valente, decidi separar, pois cada parte possui um motivo de mudança diferente. A lógica de negócio pode mudar sem afetar a notificação, e vice-versa.

Assim, a decisão foi baseada na separação por responsabilidade, garantindo maior organização e menor acoplamento.

## Aula 06 — Verificação de LSP

As subclasses Notebook, Projetor e Cabo respeitam o contrato da classe base Equipamento.

O método calcular_multa(0) retorna 0.0 em todas as subclasses.

O método calcular_multa(-5) também retorna 0.0 sem lançar exceções inesperadas.

Todas retornam valores float não negativos, mantendo o comportamento esperado pelo ServicoEmprestimo.

Portanto, o princípio LSP está satisfeito.

## Aula 06 — DIP

Com a aplicação do DIP, o ServicoEmprestimo deixou de criar suas próprias dependências e passou apenas a recebê-las pelo construtor.

Isso reduziu o acoplamento entre os módulos e tornou o sistema mais flexível e testável. Agora é possível utilizar implementações falsas de repositório e notificador para testar o serviço de forma isolada.

A mudança não foi apenas técnica, mas também conceitual, pois o controle das dependências deixou de estar dentro do serviço e passou para o módulo principal da aplicação.

Segundo Valente, no Capítulo 5, a inversão de dependência reduz o acoplamento e facilita manutenção e testes do sistema.