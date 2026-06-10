# Decomposição em camadas

## models/

### Equipamento
Representa os dados do equipamento e mantém apenas informações da entidade.

### Emprestimo
Representa os dados do empréstimo realizados no sistema.

---

## services/

### ServicoEmprestimo
Responsável pelas regras de negócio do empréstimo.

### Notificador
Responsável apenas pelo envio de notificações.

---

## repositories/

### RepositorioEmprestimo
Responsável por salvar, buscar e atualizar os dados.

---

## main.py

### main
Responsável pela interação com o atendente.

# Diagramas de sequência

## UC01 — Registrar Empréstimo

```mermaid
sequenceDiagram
    actor Atendente
    participant main as main.py
    participant servico as ServicoEmprestimo
    participant repo as RepositorioEmprestimo
    participant notif as Notificador

    Atendente->>main: informa equip_id, nome, email, dias
    main->>servico: registrar(equip_id, nome, email, dias)
    servico->>repo: buscar_equipamento(equip_id)
    repo-->>servico: Equipamento

    alt equipamento disponível
        servico->>repo: salvar_emprestimo(emprestimo)
        servico->>repo: marcar_indisponivel(equip_id)
        servico->>notif: notificar_emprestimo(email, data_devolucao)
        servico-->>main: True
    else equipamento indisponível
        servico-->>main: False
    end
```

## UC02 — Registrar Devolução

```mermaid
sequenceDiagram
    actor Atendente
    participant main as main.py
    participant servico as ServicoEmprestimo
    participant repo as RepositorioEmprestimo

    Atendente->>main: informa emprestimo_id
    main->>servico: registrar_devolucao(emprestimo_id)

    servico->>repo: buscar_emprestimo(emprestimo_id)
    repo-->>servico: Emprestimo

    alt empréstimo encontrado
        servico->>repo: marcar_disponivel(equip_id)
        servico->>repo: finalizar_emprestimo(emprestimo_id)
        servico-->>main: True
    else empréstimo não encontrado
        servico-->>main: False
    end
```

## UC03 — Listar Empréstimos em Atraso

```mermaid
sequenceDiagram
    actor Atendente
    participant main as main.py
    participant servico as ServicoEmprestimo
    participant repo as RepositorioEmprestimo

    Atendente->>main: solicitar atrasados
    main->>servico: listar_atrasados()

    servico->>repo: buscar_emprestimos()
    repo-->>servico: lista_emprestimos

    loop para cada empréstimo
        servico->>servico: verificar_atraso()
    end

    servico-->>main: lista_atrasados

## Diagrama de classes — v2.0