import os
import sys
###################################
import dotenv # .env 파일 사용
import telegram_module as MessageModule # 텔레그램 모듈
import twitter_module as twitter # 트위터 모듈
###################################

def main():
	dotenv.load_dotenv()

	telegramBotToken = os.getenv('telegramToken')
	telegramChatID = os.getenv('telegramChatID')

	twitterAPIToken = os.getenv('twitterAPItoken')
	
	# initialize Telegram Bot Module
	bot = MessageModule.TelegramBot(telegramBotToken, telegramChatID)
	# initialize bot functions
	bot.HandlerInitialize()
	# bot start updates
	bot.updater.start_polling()
	bot.updater.idle()

if __name__ == '__main__':
	main()
	os.execl(sys.executable, sys.executable, *sys.argv) # 에러 시 