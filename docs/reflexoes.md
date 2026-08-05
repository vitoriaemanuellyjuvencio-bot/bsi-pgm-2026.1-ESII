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

## Aula 09 — TDD

O TDD e o BDD possuem objetivos semelhantes, porém atendem públicos diferentes. O TDD é mais voltado para os desenvolvedores, pois utiliza testes automatizados para validar o comportamento do sistema durante a implementação. Já o BDD utiliza uma linguagem mais próxima da linguagem natural, facilitando a comunicação entre desenvolvedores, clientes e demais interessados no projeto.

Na minha opinião, o cenário BDD comunica melhor com um cliente não técnico, pois sua estrutura em Dado, Quando e Então é mais fácil de entender e representa situações reais de uso do sistema. Por outro lado, o TDD é mais eficiente para garantir a qualidade do código e detectar erros rapidamente durante o desenvolvimento.

Eu utilizaria BDD para discutir requisitos e regras de negócio com clientes e TDD para implementar e validar essas regras de forma automatizada. Dessa forma, ambos se complementam e contribuem para o desenvolvimento de um software mais confiável e alinhado às necessidades dos usuários.

## Aula 12 — Refactoring e Code Smells

[cite_start]Durante a atividade, a execução contínua do `pytest` atuou como uma verdadeira rede de segurança[cite: 77, 211]. [cite_start]Ao substituir a estrutura baseada em dicionários pela `@dataclass Evento`, a suíte de testes confirmou imediatamente que o comportamento observável do sistema foi preservado[cite: 71, 317, 322]. [cite_start]Refatorar com testes garante *feedback* instantâneo e a manutenção estrita do comportamento do software, enquanto refatorar sem testes constitui um processo de reescrita no escuro, com elevado risco de introduzir regressões não detetadas[cite: 74, 78, 80].

[cite_start]Além disso, a análise do código identificou um falso positivo [cite: 108, 340][cite_start]: as subclasses `Notebook`, `Projetor` e `Cabo` ficaram esvaziadas (`pass`) após a aplicação do padrão *Strategy* na Aula 11[cite: 339]. [cite_start]Embora a ausência de comportamento próprio lhes atribua a aparência de um *code smell* do tipo *Data Class* [cite: 108, 340][cite_start], elas desempenham o papel intencional de rótulos de tipo[cite: 341]. [cite_start]Se fosse aplicado o refactoring *Inline Class* para as dissolver, o Princípio do Aberto/Fechado (OCP) alcançado anteriormente seria revertido e violado[cite: 342]. [cite_start]Como aponta Valente (Cap. 9), nem todo sinal estrutural exige correção [cite: 219, 345][cite_start]; reconhecer quando manter uma estrutura por razões de *design* é tão relevante quanto aplicar um refactoring[cite: 345].