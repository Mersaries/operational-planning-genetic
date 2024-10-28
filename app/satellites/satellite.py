from dataclasses import dataclass
from datetime import datetime
import numpy as np


@dataclass
class OrbitElements:
    a: float  # semi-major axis [km]
    i: float  # inclination [rad]
    e: float  # eccentricity
    raan: float  # ascending node [rad]
    om: float  # argument of periapsis [rad]
    u: float  # argument of latitude


@dataclass
class StateVector:
    x: float
    y: float
    z: float
    vx: float
    vy: float
    vz: float


@dataclass
class Satellite:
    elements: OrbitElements
    state_vector: StateVector
    epoch: datetime


def from_elements_to_j2000(elements: OrbitElements) -> StateVector:
    p: float = elements.a * (1 - elements.e**2)
    r: float = p / (1 + elements.e * np.cos(elements.u - elements.om))
    x: float = r * (
        np.cos(elements.om) * np.cos(elements.u)
        - np.sin(elements.om) * np.sin(elements.u) * np.cos(elements.i)
    )
    y: float = r * (
        np.sin(elements.om) * np.cos(elements.u)
        + np.cos(elements.om) * np.sin(elements.u) * np.cos(elements.i)
    )
    z: float = r * np.sin(elements.u) * np.sin(elements.i)
    vx: float = 0
    vy: float = 0
    vz: float = 0

    return StateVector(x, y, z, vx, vy, vz)
