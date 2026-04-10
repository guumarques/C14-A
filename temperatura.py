class TemperatureConverter:
    def _check(self, value, min_val=None):
        if isinstance(value, bool):
            raise TypeError("Valor deve ser numérico (inteiro ou float), não booleano")
        if not isinstance(value, (int, float)):
            raise TypeError("Valor deve ser numérico")
        if min_val is not None and value < min_val:
            raise ValueError(f"Valor deve ser maior ou igual a {min_val}")

    def celsius_to_kelvin(self, c):
        self._check(c, -273.15)
        return round(c + 273.15, 2)

    def kelvin_to_celsius(self, k):
        self._check(k, 0)
        return round(k - 273.15, 2)

    def celsius_to_fahrenheit(self, c):
        self._check(c)
        return round(c * 9 / 5 + 32, 2)

    def fahrenheit_to_celsius(self, f):
        self._check(f)
        return round((f - 32) * 5 / 9, 2)