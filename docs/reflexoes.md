## Aula 04 — SRP

A parte mais difícil foi separar a responsabilidade de notificação da lógica de empréstimos, pois ambas acontecem no mesmo fluxo.

A dificuldade surgiu porque, ao registrar ou devolver um empréstimo, o sistema também envia uma mensagem, o que dá a impressão de que tudo deve ficar junto.

No entanto, com base no conceito de SRP apresentado por Valente, decidi separar, pois cada parte possui um motivo de mudança diferente. A lógica de negócio pode mudar sem afetar a notificação, e vice-versa.

Assim, a decisão foi baseada na separação por responsabilidade, garantindo maior organização e menor acoplamento.