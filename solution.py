import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 672508499 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    return (alpha*0.014 + 0.028 + max(x))/p, \
           (p*0.014 + 0.028 + min(x))/(alpha)
