print("BOLETIM DE NOTAS")

nome = input ("Nome do(a) aluno(a):")
curso = input ("Curso:")
semestre = input ("Semestre:")
disciplina = input ("Disciplina:")
nota = int (input ("Nota Obtida:"))

if nota >= 60 and nota <=100:
    print ("APROVADO!")
elif nota <=20:
    print ("REPROVADO!") 
else:
    print("RECUPERAÇÃO!")       
