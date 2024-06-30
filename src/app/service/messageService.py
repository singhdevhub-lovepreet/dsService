from app.utils.messagesUtil import MessagesUtil
from app.service.llmService import LLMService

class MessageService:
    def __init__(self):
        self.messageUtil = MessagesUtil()
        self.llmService = LLMService()
    
    def process_message(self, message):
        if self.messageUtil.isBankSms(message):
            return self.llmService.runLLM(message)
        else:
            return None