import pandas as pd
import numpy as np


chat_id = 201321241 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    
    return np.mean(x) > 300*1.04 # Ваш ответ, True или False
