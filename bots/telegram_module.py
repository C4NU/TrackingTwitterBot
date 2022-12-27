import telegram

from telegram.ext import Updater, dispatcher
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters

class TelegramBot:
	# 클래스 생성자
	def __init__(self, _token, _chatID):
		self.bot = telegram.Bot(token=_token)
		self.chatID = _chatID
		self.updater = Updater(token=_token, use_context=True)
		self.dispatcher = self.updater.dispatcher
	# 봇 시작 함수
	def StartBot(self, update, context):
		self.bot.sendMessage(chat_id=self.chatID, text="Starting Bot...")
	# 봇 정지 함수
	def StopBot(self, update, context):
		self.bot.sendMessage(chat_id=self.chatID, text="Quiting Bot...")
	# 계정 / 해시태그 트래킹 입력 함수
	def SetTracker(self, update, context):
		# 버튼 생성
		taskButtons = [[
			telegram.InlineKeyboardButton('Account', callback_data = 1),
			telegram.InlineKeyboardButton('Hash Tag', callback_data = 2)
		],[
			telegram.InlineKeyboardButton('Cancel', callback_data= 3)
		]]
		# 버튼 callback 입력받을 변수
		reply = telegram.InlineKeyboardMarkup(taskButtons)
		# 버튼 입력하라고 메시지 작성
		context.bot.sendMessage(
			chat_id=update.effective_chat.id,
			text="팔로우 할 것을 선택해주세요.",
			reply_markup = reply)

	def CallbackButton(self, update, context):
		query = update.callback_query
		data = query.data

		context.bot.send_chat_action(
			chat_id = update.effective_user.id,
			action = telegram.ChatAction.TYPING
		)

		if data == 1:
			self.SetTrackingAccount(query = query, data = data)
		elif data == 2:
			self.SetTrackingHashtag(query = query, data = data)
		elif data == 3:
			self.GetTrackingObjects(query = query, data = data)

		context.bot.edit_message_text(
			chat_id=query.message.chat_id,
			message_id = query.message.message_id,
			text = '[{}] Task Complete.'.format(data)
		)
	
	def SetTrackingAccount(self, update, context, query, data):
		
		context.bot.edit_message_text(
		chat_id=query.message.chat_id,
		message_id = query.message.message_id,
		text = '[{}] Task Complete.'.format(data)
		)
	
	def SetTrackingHashTag(self, update, context, query, data):
		context.bot.edit_message_text(
		chat_id=query.message.chat_id,
		message_id = query.message.message_id,
		text = '[{}] Task Complete.'.format(data)
		)

	def GetTrackingObjects(self, update, context, query, data):
		print("Get Tracking Objects..")
	
	



	# CommandHandler 생성 함수
	def HandlerInitialize(self):
		# Handler 정의 (텔레그램 /"명령어" 인삭)
		self.startHandler = CommandHandler('start', self.StartBot)
		self.stopHandler = CommandHandler('stop', self.StopBot)
		self.SetTrackerHandler = CommandHandler('set', self.SetTracker)
		self.CallBackButtonHandler = CallbackQueryHandler(self.CallbackButton)
		# Handler 추가
		self.dispatcher.add_handler(self.startHandler)
		self.dispatcher.add_handler(self.stopHandler)
		self.dispatcher.add_handler(self.SetTrackerHandler)
		self.dispatcher.add_handler(self.CallBackButtonHandler)