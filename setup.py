from setuptools import setup


setup(
    name = "data_science_interview_chatbot", # nombre de la app
    version = "0.0.1",  # version de la app
    packages = ["src"], # paquetes que publica o utiliza
    entry_points = {"console_scripts":["app = src.main:main"]}, # puntos de entrada, por donde vamos a llamar a la aplicacion.
    install_requires = open("requirements.txt").read().splitlines() # Paquetes  que se requieren
)