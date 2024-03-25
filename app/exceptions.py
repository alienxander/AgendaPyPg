class ConnectionException(Exception):
    def __init__(self, menssage = "Error en la conexión") -> None:
        self.message = menssage
    
    def __str__(self) -> str:
        return f"[ConnectionException]: {self.message}"