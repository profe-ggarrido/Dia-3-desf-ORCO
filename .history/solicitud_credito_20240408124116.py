class SolicitudCredito:
    def validar_monto(self, monto: int):
        if monto < 1000000:
            return 1000000
        elif monto > 5000000:
            return 5000000
        else:
            return monto

    def validar_correo(self, correo: str):
        terminaciones = (".cl", ".com")
        if correo.count("@") == 1 and correo.endswith(terminaciones):
            return correo
        else:
            return ""
