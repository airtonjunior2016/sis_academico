# 🎓 **Principais Classes do Sistema Acadêmico**

**ALUNOS**: :rocket:
* Francisco Airton Araujo Junior - 2023010960 (Responsável pela interface CLI)
* Francisco Eduardo da Silva - 2023009600 (Responsável pelo README e RELATÓRIO)
* Ismael Gomes da Silva - 2023011143 (Responsável pelo README e RELATÓRIO)
* Rodrigo Bezerra Nunes - 2023018707 (Responsável pela interface CLI)

O sistema utiliza **dataclasses** para representar as entidades principais do domínio acadêmico. Cada classe corresponde a uma tabela no banco SQLite e encapsula informações essenciais do sistema.

### 🔹 **1. `Curso`**

Representa um curso oferecido pela instituição.

Atributos:

- `codigo` — Identificador único do curso
- `nome` — Nome completo do curso
- `prerequisitos` — Lista de códigos de cursos exigidos (JSON)

Função no sistema:

- Serve como base para definir turmas
- Controla pré-requisitos na matrícula

---

### 🔹 **2. `Turma`**

Representa uma turma específica vinculada a um curso.

Atributos:

- `codigo` — Identificador único da turma
- `curso_codigo` — Código do curso associado
- `professor` — Nome do professor responsável
- `horario` — Horário da turma
- `limite_vagas` — Capacidade máxima
- `vagas_ocupadas` — Contador de alunos já matriculados

Função no sistema:

- Usada para matrículas, detecção de conflitos e listar ofertas de curso

---

### 🔹 **3. `Aluno`**

Representa um aluno cadastrado no sistema.

Atributos:

- `matricula` — Identificador único do aluno
- `nome` — Nome completo do aluno

Função no sistema:

- Base para matrícula
- Utilizada nos relatórios e histórico

---

### 🔹 **4. `Matricula`**

Registra a matrícula de um aluno em uma turma.

Atributos:

- `aluno_matricula` — Referência ao aluno
- `turma_codigo` — Referência à turma
- `nota` — Nota final (opcional)
- `frequencia` — Frequência final (opcional)

Função no sistema:

- Permite registrar notas, frequência e gerar histórico
- Importante para cálculo do CR
- Conecta aluno ↔ turma

---

### 🏛 **Herança**

Todas as classes herdam de:

### 🔸 `EntidadeBase`

Fornece:

- `__repr__` automático
- Ajuda na depuração e logging de entidades
