
"""gerador de rotas eleatorias"""

import random
lugares= ['escola','casa','praça']
rota= random.sample(lugares, len(lugares))

print("rota gerada:","->".join(rota))