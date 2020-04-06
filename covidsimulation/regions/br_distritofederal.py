import numpy as np

from ..age_group import AgeGroup
from ..disease_parameters import OUTCOME_THRESHOLDS
from ..parameters import Parameters
from ..simulation import SimulationConstants


age_structure = {
    '0-9': 0.151656842356445,
    '10-19': 0.170983020027698,
    '20-29': 0.2000753625027,
    '30-39': 0.1811241095067,
    '40-49': 0.134175460217207,
    '50-59': 0.085097706956155,
    '60-69': 0.045928083934799,
    '70-79': 0.022157557469572,
    '80+': 0.008801857028724
}

total_inhabitants = 2648532

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


PROPENSAO_ISOLAMENTO_PUBLICO_C = -0.6
PROPENSAO_ISOLAMENTO_PUBLICO_DE = -1.2


PUBLICO_DE = {
    'probabilidade_faixas': np.array(list(age_structure.values())),
    'risco_faixas': [
      AgeGroup(i, OUTCOME_THRESHOLDS[i], PROPENSAO_ISOLAMENTO_FAIXA[i] + PROPENSAO_ISOLAMENTO_PUBLICO_DE, 0.75)
        for i, nome_faixa in enumerate(age_structure.keys())
    ],
    'tamanho_casas': np.array([
      0.3,   # 1p
      0.25,  # 2p
      0.25,  # 3p
      0.2,   # 4p
    ]),
    'habitantes': total_inhabitants * 0.21,
    'deslocamento': 1.6,  # deslocamento geográfico
    'infectados_iniciais': 0,
}


PUBLICO_C = {
    'probabilidade_faixas': np.array(list(age_structure.values())),
    'risco_faixas': [
      AgeGroup(i, OUTCOME_THRESHOLDS[i], PROPENSAO_ISOLAMENTO_FAIXA[i] + PROPENSAO_ISOLAMENTO_PUBLICO_C, 0.92)
        for i, nome_faixa in enumerate(age_structure.keys())
    ],
    'tamanho_casas': np.array([
      0.3,   # 1p
      0.25,  # 2p
      0.25,  # 3p
      0.2,   # 4p
    ]),
    'habitantes': total_inhabitants * 0.5,
    'deslocamento': 0.8,  # deslocamento geográfico
    'infectados_iniciais': 1,
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
    'habitantes': total_inhabitants * 0.29,
    'leitos_uti': 929,  
    'deslocamento': 0.0,  # deslocamento geográfico
    'infectados_iniciais': 6,
}


population_segments = {'privado': PRIVADO, 'publico_c': PUBLICO_C, 'publico_de': PUBLICO_DE}


params = Parameters(
    population_segments,
    SimulationConstants(),
    d0_infections=1500,
    start_date='2020-03-11',
    capacity_hospital_max=60000,
    capacity_hospital_beds=6705,
    capacity_intensive_care=1273,
    capacity_ventilators=2100,
    transmission_scale_days=0.3,
    min_age_group_initially_infected=4,
)
