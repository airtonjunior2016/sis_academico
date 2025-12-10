# ============================
#   SISTEMA ACADÊMICO – COLAB
# ============================

import sqlite3
import json
from dataclasses import dataclass, field
from typing import List, Optional


# ============================
# DATABASE
# ============================

DB_NAME = "gestor_academico.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def inicializar():
    con = conectar()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS cursos (
            codigo TEXT PRIMARY KEY,
            nome TEXT,
            prerequisitos TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS turmas (
            codigo TEXT PRIMARY KEY,
            curso_codigo TEXT,
            professor TEXT,
            horario TEXT,
            limite_vagas INTEGER,
            vagas_ocupadas INTEGER
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            matricula TEXT PRIMARY KEY,
            nome TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS matriculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_matricula TEXT,
            turma_codigo TEXT,
            nota REAL,
            frequencia REAL
        )
    """)

    con.commit()
    con.close()


# ============================
# MODELOS
# ============================

class EntidadeBase:
    def __repr__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"

@dataclass
class Curso(EntidadeBase):
    codigo: str
    nome: str
    prerequisitos: List[str] = field(default_factory=list)

@dataclass
class Turma(EntidadeBase):
    codigo: str
    curso_codigo: str
    professor: str
    horario: str
    limite_vagas: int
    vagas_ocupadas: int = 0

@dataclass
class Aluno(EntidadeBase):
    matricula: str
    nome: str

@dataclass
class Matricula(EntidadeBase):
    aluno_matricula: str
    turma_codigo: str
    nota: Optional[float] = None
    frequencia: Optional[float] = None


# ============================
# SERVICOS
# ============================

def curso_por_codigo(codigo):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT codigo, nome, prerequisitos FROM cursos WHERE codigo=?", (codigo,))
    row = cur.fetchone()
    con.close()
    return Curso(row[0], row[1], json.loads(row[2])) if row else None

def turma_por_codigo(codigo):
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        SELECT codigo, curso_codigo, professor, horario, limite_vagas, vagas_ocupadas
        FROM turmas WHERE codigo=?
    """, (codigo,))
    row = cur.fetchone()
    con.close()
    return Turma(*row) if row else None

def aluno_por_matricula(m):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT matricula, nome FROM alunos WHERE matricula=?", (m,))
    row = cur.fetchone()
    con.close()
    return Aluno(*row) if row else None

def horarios_conflitam(h1, h2):
    return h1 == h2  # versão simples

def aluno_tem_prerequisitos(aluno_matricula, curso: Curso):
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        SELECT t.curso_codigo
        FROM matriculas m
        JOIN turmas t ON t.codigo = m.turma_codigo
        WHERE m.aluno_matricula=? AND m.nota >= 6
    """, (aluno_matricula,))
    historico = {row[0] for row in cur.fetchall()}
    con.close()
    return all(pr in historico for pr in curso.prerequisitos)

def matricular(aluno_matricula, turma_codigo):
    aluno = aluno_por_matricula(aluno_matricula)
    turma = turma_por_codigo(turma_codigo)

    if not aluno:
        return "Aluno não encontrado."
    if not turma:
        return "Turma não encontrada."

    curso = curso_por_codigo(turma.curso_codigo)

    if not aluno_tem_prerequisitos(aluno_matricula, curso):
        return "Aluno não possui pré-requisitos."

    if turma.vagas_ocupadas >= turma.limite_vagas:
        return "Turma sem vagas."

    con = conectar()
    cur = con.cursor()
    cur.execute("""
        SELECT t.horario
        FROM matriculas m
        JOIN turmas t ON t.codigo = m.turma_codigo
        WHERE aluno_matricula=?
    """, (aluno_matricula,))

    for (horario,) in cur.fetchall():
        if horarios_conflitam(horario, turma.horario):
            return "Conflito de horário."

    # Efetivar
    cur.execute("INSERT INTO matriculas (aluno_matricula, turma_codigo) VALUES (?,?)",
                (aluno_matricula, turma_codigo))
    cur.execute("UPDATE turmas SET vagas_ocupadas=vagas_ocupadas+1 WHERE codigo=?",
                (turma_codigo,))
    con.commit()
    con.close()

    return "Matrícula realizada com sucesso!"

def registrar_nota(matricula, turma, nota):
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        UPDATE matriculas SET nota=? WHERE aluno_matricula=? AND turma_codigo=?
    """, (nota, matricula, turma))
    con.commit()
    con.close()
    return "Nota registrada."

def registrar_frequencia(matricula, turma, freq):
    con = conectar()
    cur = conectar().cursor()
    cur.execute("""
        UPDATE matriculas SET frequencia=? WHERE aluno_matricula=? AND turma_codigo=?
    """, (freq, matricula, turma))
    conectar().commit()
    return "Frequência registrada."

def relatorio_historico(matricula):
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        SELECT t.curso_codigo, m.nota, m.frequencia
        FROM matriculas m
        JOIN turmas t ON t.codigo = m.turma_codigo
        WHERE aluno_matricula=?
    """, (matricula,))
    dados = cur.fetchall()
    con.close()
    return dados


# ============================
# CLI (compatível com Colab)
# ============================

def adicionar_curso():
    codigo = input("Código do curso: ")
    nome = input("Nome: ")
    prereq = input("Pré-requisitos (separados por vírgula): ").split(",")

    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO cursos VALUES (?,?,?)", (codigo, nome, json.dumps([p for p in prereq if p])))
    con.commit()
    con.close()
    print("Curso cadastrado.")

def adicionar_turma():
    codigo = input("Código da turma: ")
    curso = input("Curso: ")
    prof = input("Professor: ")
    horario = input("Horário (ex: seg-10-12): ")
    limite = int(input("Limite de vagas: "))

    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO turmas VALUES (?,?,?,?,?,?)",
                (codigo, curso, prof, horario, limite, 0))
    con.commit()
    con.close()
    print("Turma cadastrada.")

def adicionar_aluno():
    matricula = input("Matrícula: ")
    nome = input("Nome do aluno: ")

    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO alunos VALUES (?,?)", (matricula, nome))
    con.commit()
    con.close()
    print("Aluno cadastrado.")

def menu():
    while True:
        print("\n=== MENU DO SISTEMA ACADÊMICO ===")
        print("1. Adicionar curso")
        print("2. Adicionar turma")
        print("3. Adicionar aluno")
        print("4. Matricular aluno")
        print("5. Registrar nota")
        print("6. Registrar frequência")
        print("7. Histórico do aluno")
        print("0. Sair")

        op = input("Escolha: ")

        if op == "1":
            adicionar_curso()
        elif op == "2":
            adicionar_turma()
        elif op == "3":
            adicionar_aluno()
        elif op == "4":
            m = input("Matrícula: ")
            t = input("Turma: ")
            print(matricular(m, t))
        elif op == "5":
            m = input("Matrícula: ")
            t = input("Turma: ")
            nota = float(input("Nota: "))
            print(registrar_nota(m, t, nota))
        elif op == "6":
            m = input("Matrícula: ")
            t = input("Turma: ")
            f = float(input("Frequência: "))
            print(registrar_frequencia(m, t, f))
        elif op == "7":
            m = input("Matrícula: ")
            hist = relatorio_historico(m)
            print("\n=== HISTÓRICO ===")
            for c, n, f in hist:
                print(f"Curso: {c} | Nota: {n} | Frequência: {f}")
        elif op == "0":
            print("Encerrado.")
            break
        else:
            print("Opção inválida.")


# Inicializar banco automaticamente
inicializar()

print("Sistema carregado! Execute:  menu()  para iniciar.")

menu()
