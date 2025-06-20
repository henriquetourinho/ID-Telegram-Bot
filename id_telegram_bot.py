import logging
import signal
import sys

from telegram import Update
# Corrigido: Importar ChatAction de telegram.constants
from telegram.constants import ChatAction 
from telegram import MessageOriginUser, MessageOriginChat, MessageOriginHiddenUser
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


# --- Constantes para Mensagens ---
START_MESSAGE = (
    "Olá! 👋 Eu sou o **ID Telegram Bot**.\n\n"
    "➡️ Para saber o seu ID, apenas me envie qualquer mensagem.\n\n"
    "➡️ Para saber o ID de outra pessoa, encaminhe uma mensagem dela para mim."
)
USER_ID_MESSAGE = "Olá, **{full_name}**!\nO seu ID do Telegram é: `{user_id}`"
FORWARDED_USER_ID_MESSAGE = "A mensagem encaminhada é de: **{full_name}**\nO ID dele(a) é: `{user_id}`"
HIDDEN_USER_MESSAGE = "A mensagem foi encaminhada de: **{user_name}**\nO ID está protegido devido às configurações de privacidade do usuário."
CHANNEL_FORWARD_MESSAGE = (
    f"Você, **{{forwarder_name}}**, encaminhou uma mensagem do canal **{{chat_title}}**.\n\n"
    f"ℹ️ **ID do Canal:** `{{chat_id}}`\n"
    f"👤 **O seu ID (quem encaminhou):** `{{forwarder_id}}`"
)
UNKNOWN_FORWARD_MESSAGE = "A mensagem foi encaminhada, mas não foi possível determinar a origem exata."
ERROR_MESSAGE = "Ocorreu um erro ao processar sua solicitação. Por favor, tente novamente."

# Substitua "SEU_TOKEN_AQUI" pelo token que você pegou do @BotFather
TOKEN = "SEU_TOKEN_AQUI"

# Configura o logging para ver erros
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Função para o comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia uma mensagem de boas-vindas."""
    try:
        await update.message.reply_text(START_MESSAGE, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Erro ao enviar mensagem de start: {e}")
        await update.message.reply_text(ERROR_MESSAGE)


# Função principal que lida com as mensagens
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde com o ID correto dependendo se a mensagem é direta ou encaminhada."""
    try:
        # Envia a ação de digitação para o usuário
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

        origin = update.message.forward_origin
        
        if origin:
            # CASO 1: Encaminhado de um usuário normal
            if isinstance(origin, MessageOriginUser):
                user = origin.sender_user
                await update.message.reply_text(
                    USER_ID_MESSAGE.format(full_name=user.full_name, user_id=user.id), # Usado USER_ID_MESSAGE para consistência
                    parse_mode='Markdown'
                )
            # CASO 2: Encaminhado de um usuário com privacidade ativada
            elif isinstance(origin, MessageOriginHiddenUser):
                user_name = origin.sender_user_name
                await update.message.reply_text(
                    HIDDEN_USER_MESSAGE.format(user_name=user_name),
                    parse_mode='Markdown'
                )
            # CASO 3: Encaminhado de um canal ou grupo
            elif isinstance(origin, MessageOriginChat):
                forwarder = update.message.from_user
                chat = origin.sender_chat
                await update.message.reply_text(
                    CHANNEL_FORWARD_MESSAGE.format(
                        forwarder_name=forwarder.full_name,
                        chat_title=chat.title,
                        chat_id=chat.id,
                        forwarder_id=forwarder.id
                    ),
                    parse_mode='Markdown'
                )
            # CASO 4: Fallback para qualquer outra situação
            else:
                await update.message.reply_text(UNKNOWN_FORWARD_MESSAGE)
        # Se for uma mensagem normal (não encaminhada)
        else:
            sender_user = update.message.from_user
            await update.message.reply_text(
                USER_ID_MESSAGE.format(full_name=sender_user.full_name, user_id=sender_user.id),
                parse_mode='Markdown'
            )
    except Exception as e:
        logger.error(f"Erro ao processar mensagem: {e}")
        await update.message.reply_text(ERROR_MESSAGE)

def main() -> None:
    """Inicia o bot."""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))
    
    # Adiciona um manipulador de sinal para encerrar graciosamente
    def signal_handler(signum, frame):
        logger.info("Sinal de encerramento recebido. Parando o bot...")
        application.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    print("Bot iniciado... Pressione Ctrl+C para parar.")
    application.run_polling()

if __name__ == "__main__":
    main()