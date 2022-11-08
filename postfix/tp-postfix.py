#!/usr/bin/env python
# coding: utf-8

# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span><img src="media/both-logos-small-alpha.png" /></span>
# </div>

# # calculette postfix

# In[ ]:


# ceci permet de recharger les modules
# lorsqu'ils ont été modifiés en dehors du notebook

# pour commodité lors du développement des exercices

get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# ****

# ## Évaluateur d'expression postfix

# Une fonction `postfix_eval` prend en entrée une chaîne qui décrit une opération à faire sur des entiers, en utilisant **la notation polonaise postfixée**, où on écrit par exemple `10 20 +` pour ajouter 10 et 20 ; cette notation est aussi appelée la **notation polonaise inverse**.
# 
# Les opérandes sont tous des entiers ; on demande de supporter les 4 opérations `+` `-` `*` et `/` (division entière), la calculatrice ne manipule donc que des entiers.
# 
# Lorsque la chaine est mal formée, vous devez renvoyer une des trois chaines suivantes :
# 
# * `error-syntax` si on ne peut pas comprendre l'entrée,
# * `error-empty-stack`, si on essaie de faire une opération mais que l'on n'a pas les deux opérandes nécessaires,
# * `error-unfinished`, si on détecte des opérandes non utilisés.

# In[ ]:


# charger l'exercice et afficher un exemple
from corrections.exo_postfix_eval import exo_postfix_eval
exo_postfix_eval.example()


# In[ ]:


operators= '+-*/'

def postfix_eval(chaine):
    stack = []
    for token in chaine.strip().split(' '):
        if token in operators:
            if len(stack)<2:
                return('error-empty-stack')
            else:
                rhs = stack.pop()
                lhs = stack.pop()
                if token == '+':
                    result = rhs + lhs
                elif token == '-':
                    result = lhs - rhs
                elif token == '*':
                    result = rhs * lhs
                elif token == '/':
                    result = lhs // rhs
            stack.append(int(result))
        else:
            try:
                stack.append(int(token))
            except:
                return('error-syntax')
    if len(stack) != 1:
        return('error-unfinished')
    else:
        return(stack[0])
    
        


# In[ ]:


exo_postfix_eval.correction(postfix_eval)


# ****

# ## Évaluateur d'expression postfix typé
# 
# Une variante un peu plus difficile

# Écrire une variante de `postfix_eval` qui accepte en deuxième argument un type de nombre parmi `int`, `float`, ou `Fraction`, de sorte que la calculette utilise ce type pour faire ses calculs.
# 
# **indice :** attention au cas de la division, qui doit se comporter selon le type comme une division entière (comme dans `postfix_eval`), ou comme une division usuelle si le type le permet.

# In[ ]:


from fractions import Fraction


# In[ ]:


# charger l'exercice et afficher un exemple

from corrections.exo_postfix_eval import exo_postfix_eval_typed
exo_postfix_eval_typed.example()


# In[ ]:


# votre code
def postfix_eval_typed(chaine, result_type):
    ...


# In[ ]:


exo_postfix_eval_typed.correction(postfix_eval_typed)


# ****
