from whatsapp_api_client_python import API
import logging, os
from datetime import datetime
from colorama import Fore, Style, init
from dotenv import load_dotenv

load_dotenv()
init()

greenAPI = API.GreenAPI(
    os.getenv("INSTANCE_ID"), os.getenv("INSTANCE_API_KEY")
)
class Client:


    class Message:
        def __init__(self):
            self.body = None
            self.phone_number = None

        def send(self, message: str):
            return greenAPI.sending.sendMessage(self.phone_number, message)
    
    class Msg:
        def __init__(self):
            self.prefix = None
            self.command = None
            self.args = None
            
            
    def __init__(self):
        self.message = self.Message()
        self.commands = {}
        self.prefix = []
        
        self.msg = self.Msg()
        self._setup_logging()
    
    def set_prefix(self, prefix: str|list):
        if isinstance(prefix, str):
            self.prefix.append(prefix)

        elif isinstance(prefix, list):
            self.prefix = prefix

    def _parse_message(self, text: str):
        prefixes = self.prefix
        
        for prefix in prefixes:
            if text.startswith(prefix):
                text = text[len(prefix):]
                self.msg.prefix = prefix
                break
        else:
            return None, None, None

        parts = text.split()
        
        if not parts:
            return None, None, None
        
        self.msg.command = parts[0]
        
        self.msg.args = parts[1:]
        
    def add_command(self, command: str, function):
        self.commands[command] = function

    def _execute_command(self, command: str):
        if command in self.commands:
            func = self.commands[command]
            func(self.message.body, self.message.phone_number)

    def start(self):
        greenAPI.webhooks.startReceivingNotifications(self._handler)

    def _handler(self, type_webhook: str, body: dict) -> None:
        if type_webhook == "incomingMessageReceived":
            # Windows or Linux
            self.message.body = body["messageData"]["extendedTextMessageData"]["text"] or body["messageData"]["textMessageData"]["textMessage"]
            self.message.phone_number = body["senderData"]["sender"]
            
            self._parse_message(self.message.body)

            if any(self.message.body.startswith(prefix) for prefix in self.prefix):
                self._execute_command(self.msg.command)

    def _setup_logging(self):
        logger = logging.getLogger('whatsapp-api-client-python')
        logger.setLevel(logging.INFO)

        if logger.hasHandlers():
            logger.handlers.clear()

        handler = logging.StreamHandler()

        class CustomFormatter(logging.Formatter):
            def format(self, record):
                timestamp = datetime.now().strftime("[%m/%d/%Y %H:%M:%S]")
                if record.levelname == "INFO":
                    return f"{Fore.LIGHTBLACK_EX}{timestamp} {Fore.BLUE}{record.levelname} {Style.RESET_ALL}{record.getMessage()}"
                elif record.levelname == "ERROR":
                    return f"{Fore.LIGHTBLACK_EX}{timestamp} {Fore.RED}{record.levelname} {Style.RESET_ALL}{record.getMessage()}"
                elif record.levelname == "WARNING":
                    return f"{Fore.LIGHTBLACK_EX}{timestamp} {Fore.YELLOW}{record.levelname} {Style.RESET_ALL}{record.getMessage()}"

        formatter = CustomFormatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)