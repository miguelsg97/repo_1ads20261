def fila_tijolos(n_peq, n_gra, meta):
  graDisp = min(meta // 5, n_gra) 
  r = meta - graDisp * 5
  return n_peq >= r