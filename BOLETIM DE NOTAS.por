programa {
  funcao inicio() {
    escreva("BOLETIM DE NOTAS")

    cadeia nome
    cadeia curso
    cadeia semestre
    cadeia disciplina 
    inteiro nota 

    escreva("\n Nome do(a) Aluno(a):")
    leia (nome)


    escreva("\n Curso:")
    leia (curso)


    escreva("\n Semestre:")
    leia(semestre)

    escreva("\n Disciplina:" )
    leia(disciplina)

    escreva("\n Nota:")
    leia(nota)

    se(nota >19 e nota <60)
    {
      escreva ("RECUPERAÇÃO!")
    }

    se(nota >= 60 e nota <= 100) 
     {
      escreva ("APROVADO!")
     }

     senao se (nota <20)
    {
      escreva("REPROVADO!")
    }



  }
}
