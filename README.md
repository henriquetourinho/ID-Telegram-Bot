# 🤖 ID Telegram Bot

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

**Descubra IDs de usuários, grupos e canais do Telegram de forma simples, rápida e sem mistério!**

O **ID Telegram Bot** é um bot open source que responde imediatamente com o ID do Telegram de qualquer usuário, grupo ou canal — basta enviar ou encaminhar uma mensagem. Ideal para desenvolvedores, administradores de grupos e curiosos que precisam saber rapidamente IDs no Telegram.

![Demo do ID Telegram Bot](https://github.com/henriquetourinho/ID-Telegram-Bot/blob/main/media/demo.gif?raw=true)

---

### Sobre o Projeto

O **ID Telegram Bot** nasceu da necessidade prática de descobrir facilmente o ID do Telegram em qualquer contexto: seja para automatizar tarefas, configurar bots, gerir grupos ou simplesmente sanar uma dúvida. Com uma interface amigável e respostas claras, este bot elimina qualquer complicação — basta enviar uma mensagem ou encaminhar o que quiser identificar.

Feito com Python e [python-telegram-bot](https://python-telegram-bot.org/), o código é enxuto, moderno e pronto para rodar em qualquer servidor com Python 3.11+.

---

### 🚀 Instalação Rápida

> Você só precisa de Python 3.11+ e um token de bot Telegram (use o [@BotFather](https://t.me/BotFather) para criar o seu).

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/henriquetourinho/id-telegram-bot.git
    cd id-telegram-bot
    ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    Ou simplesmente:
    ```bash
    pip install python-telegram-bot
    ```

4. **Configure seu token:**
    - No arquivo `id-telegram-bot.py`, substitua o valor da variável `TOKEN` pelo token gerado no BotFather.

5. **Execute o bot:**
    ```bash
    python3 id-telegram-bot.py
    ```

Pronto! O bot estará rodando e pronto para uso.

---

### Funcionalidades Principais

* **Identificação Instantânea:**
    * Descubra facilmente o ID de quem te enviou mensagem.
    * Encaminhe mensagens de outros usuários, grupos ou canais para descobrir seus IDs.
    * O bot detecta privacidade de usuários e informa se o ID está oculto.

* **Mensagens customizadas e amigáveis:**  
    * Respostas claras, em português, facilitando o entendimento.

* **Código limpo, assíncrono e seguro:**  
    * Baseado em Python moderno e na robusta biblioteca `python-telegram-bot`.

---

### Exemplo de Uso

- **Para saber seu próprio ID:**  
  Basta enviar qualquer mensagem para o bot.

- **Para saber o ID de outra pessoa, grupo ou canal:**  
  Encaminhe uma mensagem dessa pessoa/grupo/canal para o bot.

---

### Roadmap & Futuro

- [ ] Suporte a múltiplos idiomas (internacionalização)
- [ ] Responder IDs de chats em fotos, vídeos e áudios encaminhados
- [ ] Deploy fácil via Docker
- [ ] Tutorial em vídeo

Sinta-se à vontade para sugerir novas funcionalidades via [issues](https://github.com/henriquetourinho/id-telegram-bot/issues)!

---

### Tech Stack

* **Linguagem:** Python 3.11+
* **Framework:** python-telegram-bot
* **Principais Bibliotecas:** `telegram`, `logging`, `signal`

---

### Requisitos

* **Python:** 3.11 ou superior
* **Token do Bot Telegram:** Gere em [@BotFather](https://t.me/BotFather)

---

### Licença

Este projeto é distribuído sob a **Licença GNU GPLv3**. Veja o arquivo `LICENSE` para mais detalhes.

---

## 🙋‍♂️ Desenvolvido por

**Carlos Henrique Tourinho Santana** 📍 Salvador - Bahia  
🔗 Wiki Debian: [wiki.debian.org/henriquetourinho](https://wiki.debian.org/henriquetourinho)  
🔗 LinkedIn: [br.linkedin.com/in/carloshenriquetourinhosantana](https://br.linkedin.com/in/carloshenriquetourinhosantana)  
🔗 GitHub: [github.com/henriquetourinho](https://github.com/henriquetourinho)

---

📢 **Este é um projeto vivo — colaborações, sugestões e novas ideias são muito bem-vindas!**