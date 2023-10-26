# Processamento de matrizes e funções matemáticas
import numpy as np
# Manipulação e análise de dados
import pandas as pd
# Plotagem de gráficos
import matplotlib.pyplot as plt
# Distribuição de dados para o treino e teste
from sklearn.model_selection import train_test_split
# Métricas
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_percentage_error

# Funções matemáticas
import math

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

# Modelling
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
# Modelos (apenas como ilustração)
from sklearn.linear_model import LinearRegression
# Localização para o Teste Online
from geopy.geocoders import Nominatim


# Executando a célula para montar o Drive
from google.colab import drive
drive.mount('/content/drive')


