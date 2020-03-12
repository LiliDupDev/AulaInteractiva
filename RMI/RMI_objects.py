import Pyro4


@Pyro4.expose
class Thermostat:

    def evaluateTemperature(self,temperature):
        if temperature < 20:
            a = 'La temperatura esta baja, lo recomendado es entre 20°C y 25°C'
            return a
        if temperature > 25:
            a = 'La temperatura esta alta, lo recomendado es entre 20°C y 25°C'
            return a
        elif temperature >= 20 & temperature <= 25:
            a = 'Esta bien k'
            return a
