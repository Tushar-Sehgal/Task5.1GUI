import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setmode(GPIO.BCM)
led_pins = {"Red" : 17, "Green" : 27, "Blue" : 22}
for pin in led_pins.values():
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

def switch_led(led_color):
	for color, pin in led_pins.items():
		GPIO.output(pin, GPIO.HIGH if color == led_color else GPIO.LOW)

root = tk.Tk()
root.title("LED Control Panel")

led_choice = tk.StringVar()
led_choice.set("Off")

for color in led_pins:
	radio_button = tk.Radiobutton(root, text = color, variable = led_choice, value = color, command = lambda: switch_led(led_choice.get()))
	radio_button.pack(anchor = tk.W)

exit_button = tk.Button(root, text="Exit", command = root.quit)
exit_button.pack(side = tk.BOTTOM)

root.mainloop()

GPIO.cleanup()
