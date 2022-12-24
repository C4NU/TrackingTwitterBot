import os
import sys
###################################
import dotenv # .env 파일 사용
import telegram_module as bot # 텔레그램 모듈
import twitter_module as twitter # 트위터 모듈
###################################

def main():
	dotenv.load_dotenv()

	token = os.getenv('token')
	chatID = os.getenv('chatID')



	telegram_bot = bot.TelegramBot(token, chatID)


if __name__ == '__main__':
	main()
	os.execl(sys.executable, sys.executable, *sys.argv)