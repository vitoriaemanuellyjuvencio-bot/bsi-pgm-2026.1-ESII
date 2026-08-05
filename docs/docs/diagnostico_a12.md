# Diagnóstico de Code Smells - Aula 12

| # | Arquivo:linha | Smell (nome técnico) | Refactoring proposto | Justificativa |
|---|---------------|-----------------------|----------------------|---------------|
| 1 | `services/servico_emprestimo.py:12` | Primitive Obsession | Replace Primitive with Object | Dicionário de evento substituído pela classe `@dataclass Evento`. |
| 2 | `services/servico_emprestimo.py:35` | Mysterious Name | Rename | Variável de uma letra renomeada para refletir sua intenção (`dias_atraso`). |
| 3 | `services/servico_emprestimo.py:50` | Long Method | Extract Function | Função longa dividida extraindo a formatação da mensagem para método auxiliar. |
| 4 | `services/notificador_email.py:8` | Comments | Extract Function + Rename | Comentário removido após renomeação clara do método e parâmetros. |
| 5 | `models/equipamentos.py:10` | Data Class (Falso Positivo) | Nenhum (Manter) | Subclasses esvaziadas pós-Strategy funcionam como rótulos de tipo. Dissolvê-las violaria o OCP. |