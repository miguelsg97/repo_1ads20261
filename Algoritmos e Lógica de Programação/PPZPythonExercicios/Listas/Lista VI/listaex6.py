def dormir(dia_semana, feriado):
  return feriado or not dia_semana

def alunos_problema(a_sorri, b_sorri):
  return a_sorri == b_sorri

def soma_dobro(a, b):
    return (a + b) * 2 if a == b else a + b

def diff21(n):
    return abs(n - 21) *  2 if n > 21 else abs(n - 21)

def papagaio(falando, hora):
  return falando and (hora < 7 or hora > 20)

def dez(a, b):
    return a == 10 or b == 10 or a + b == 10

def dista10(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

def apaga(s, n):
    return s[:n] + s[n+1:]

def troca(s):
    return s if len(s) <= 1 else s[-1] + s[1:-1] + s[0]

