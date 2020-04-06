import numpy as np

from ..age_group import AgeGroup
from ..disease_parameters import OUTCOME_THRESHOLDS
from ..parameters import Parameters
from ..simulation import SimulationConstants


age_structure = {
    '0-9': 0.128,
    '10-19': 0.159,
    '20-29': 0.167,
    '30-39': 0.158,
    '40-49': 0.139,
    '50-59': 0.115,
    '60-69': 0.071,
    '70-79': 0.041,
    '80+': 0.019
}


total_inhabitants = 11957793


PROPENSAO_ISOLAMENTO_FAIXA = [
    -0.2,  # 0
    -0.4,  # 1
    -0.2,  # 2
    -0.3,  # 3
    0.0,  # 4
    0.2,  # 5
    0.8,  # 6
    1.6,  # 7
    1.6,  # 8
]


PROPENSAO_ISOLAMENTO_PUBLICO_CD = -0.6
PROPENSAO_ISOLAMENTO_PUBLICO_E = -1.2

PUBLICO_E = {
    'probabilidade_faixas': np.array(list(age_structure.values())),
    'risco_faixas': [
      AgeGroup(i, OUTCOME_THRESHOLDS[i], PROPENSAO_ISOLAMENTO_FAIXA[i] + PROPENSAO_ISOLAMENTO_PUBLICO_E, 0.75)
        for i, nome_faixa in enumerate(age_structure.keys())
    ],
    'tamanho_casas': np.array([
      0.3,   # 1p
      0.25,  # 2p
      0.25,  # 3p
      0.2,   # 4p
    ]),
    'habitantes': total_inhabitants * 0.13,
    'deslocamento': 1.6,  # deslocamento geográfico
    'infectados_iniciais': 1,
}


PUBLICO_CD = {
    'probabilidade_faixas': np.array(list(age_structure.values())),
    'risco_faixas': [
      AgeGroup(i, OUTCOME_THRESHOLDS[i], PROPENSAO_ISOLAMENTO_FAIXA[i] + PROPENSAO_ISOLAMENTO_PUBLICO_CD, 0.92)
        for i, nome_faixa in enumerate(age_structure.keys())
    ],
    'tamanho_casas': np.array([
      0.3,   # 1p
      0.25,  # 2p
      0.25,  # 3p
      0.2,   # 4p
    ]),
    'habitantes': total_inhabitants * 0.54,
    'deslocamento': 0.8,  # deslocamento geográfico
    'infectados_iniciais': 2,
}


PRIVADO = {
    'probabilidade_faixas': np.array(list(age_structure.values())),
    'risco_faixas': [
      AgeGroup(i, OUTCOME_THRESHOLDS[i], PROPENSAO_ISOLAMENTO_FAIXA[i], 0.95)
        for i, nome_faixa in enumerate(age_structure.keys())
    ],
    'tamanho_casas': np.array([
      0.3,   # 1p
      0.3,   # 2p
      0.25,  # 3p
      0.15,  # 4p
    ]),
    'habitantes': total_inhabitants * 0.33,
    'deslocamento': 0.0,  # deslocamento geográfico
    'infectados_iniciais': 12,
}

population_segments = {'privado': PRIVADO, 'publico_cd': PUBLICO_CD, 'publico_e': PUBLICO_E}

params = Parameters(
    population_segments,
    SimulationConstants(),
    d0_infections=3200,
    start_date='2020-3-15',
    capacity_hospital_max=60000,
    capacity_hospital_beds=21000,
    capacity_intensive_care=3734,
    capacity_ventilators=4327,
    transmission_scale_days=0.3,
    min_age_group_initially_infected=4,
)
