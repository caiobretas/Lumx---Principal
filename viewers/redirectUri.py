import socket
from flask import Flask, redirect

class RedirectUri:
    
    import socket

    # Função para obter o endereço IP da rede local
    def get_local_ip_address(self):
        # Obtém o endereço IP do gateway padrão
        def get_default_gateway():
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                a = s.getsockname()[0]
                return s.getsockname()[0]

        # Cria um soquete e o conecta ao gateway padrão
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        a = s.connect((get_default_gateway(), 1))
        s.connect((get_default_gateway(), 1))

        # Obtém o endereço IP do soquete
        ip_address = s.getsockname()[0]

        # Fecha o soquete e retorna o endereço IP
        s.close()
        return ip_address


    def __init__(self) -> None:
        self.ip = self.get_local_ip_address()
        
        
        
        
        
        
        
        
    
    
    # self.host = socket.gethostname()
    # self.ip = socket.gethostbyname(self.host)

    # @app.route('/')
    # def hello():
    #     return 'Olá, mundo!'

    # if __name__ == '__main__':
    #     # Executa o aplicativo Flask no endereço IP 0.0.0.0 na porta 5000
    #     app.run(host=self.ip, port=5000)