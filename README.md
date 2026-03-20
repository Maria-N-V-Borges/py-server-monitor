# 🌐 Network Monitor (Python Polling)

Este projeto é um script robusto em Python para realizar o monitoramento de disponibilidade de múltiplos servidores simultaneamente via Polling. Desenvolvido para aplicar conceitos de Redes de Computadores e automação com Python.

## 🚀 Funcionalidades
- **Multi-Server Polling:** Monitora uma lista de URLs em um único ciclo de execução.

- **HTTP Status Analysis:** Identifica e traduz códigos de resposta (200, 404, 503, etc.) para mensagens amigáveis, seguindo a lógica de protocolos de rede.

- **Advanced Error Handling:** Diferencia entre erros de conexão (servidor offline) e erros de aplicação (URL inexistente ou proibida).

- **Event Logging:** Salva automaticamente o histórico de monitoramento em um arquivo `log_eventos.txt` com data e hora precisa.

- **User-Agent Simulation:** Evita bloqueios de segurança simulando acessos de navegadores reais.

## 🛠️ Tecnologias
- Python 3.13+
- Requests Library: Para comunicação HTTP de alto nível.
- Datetime: Para carimbo de tempo nos logs.

## 🗺️ Roadmap (Evolução do Projeto)

- [x] **Polling Básico:** Criar o loop de monitoramento de um servidor.
- [x] **Sistema de Logs:** Salvar eventos em um arquivo `.txt` com data e hora.
- [x] **Multi-Server:** Monitorar uma lista de vários sites simultaneamente.
- [x] **HTTP Status Mapping:** Traduzir códigos de erro (Dica do amigo!).
- [ ] **Ambiente Virtual (venv):** Documentar como configurar o ambiente isolado.
- [ ] **Discord/Telegram Alert:** Enviar notificações reais quando um site cair.
- [ ] **Interface Gráfica (GUI):** Criar uma janelinha para o monitor (talvez usando Tkinter).
