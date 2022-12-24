from setuptools import Command
import telegram

from telegram.ext import Updater, dispatcher
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

class TelegramBot:
	# 클래스 생성자
	def __init__(self, _token, _chatID):
		self.bot = telegram.Bot(token=_token)
		self.chatID = _chatID
		self.updater = Updater(token=_token, use_context=True)
		self.dispatcher = self.updater.dispatcher
    # 메시지 전송 함수 (self, 메시지 내용)
	def SendTelegramMessage(self, _description):
		self.bot.sendMessage(chat_id=self.chatID, text=_description)

	# 봇 시작 함수
	def StartBot(self, update, context):
		self.SendTelegramMessage("봇 작동 시작.")
	# 봇 정지 함수
	def StopBot(self, update, context):
		self.SendTelegramMessage("봇 작동 종료.")
	def SetTracker(self, update, context):
		self.SendTelegramMessage("팔로우 할 계정 \ 해시태그를 입력해주세요.")
		self.SendTelegramMessage("계정은 @를 붙이시고, 해시태그는 #을 붙이시면 됩니다.")

    # CommandHandler 생성 함수
	def HandlerInitialize(self):
		# Handler 정의 (텔레그램 /"명령어" 인삭)
		self.startHandler = CommandHandler('start', self.StartBot)
		self.stopHandler = CommandHandler('stop', self.StopBot)
		self.setTrackerHandler = CommandHandler('set', self.SetTracker)
		# Handler 추가
		self.dispatcher.add_handler(self.startHandler)
		self.dispatcher.add_handler(self.stopHandler)
		self.dispatcher.add_handler(self.setTrackerHandler)


if __name__ == '__main__':
	main()