import mido
from pynput.keyboard import Controller, Key

# Create a keyboard controller
keyboard = Controller()

def print_midi_input():
    # 利用可能なMIDIデバイスのリストを取得します
    input_names = mido.get_input_names()

    # 最初のMIDIデバイスを選択します
    # 使用するデバイスにより、この部分を適宜変更してください
    with mido.open_input(input_names[0]) as inport:
        print(f"Opened {inport} for listening MIDI signals")
        
        # 無限にMIDIメッセージを受け取り、コンソールに出力します
        # MIDIデバイスからの入力がないときは、このループはブロックされます
        for msg in inport:
            # Check if the message is control change, on channel 0 and controller number is 64
            if msg.type == 'control_change' and msg.channel == 0 and msg.control == 64:
                # If value is between 1 and 30, press the up arrow key
                if 1 <= msg.value <= 30:
                    keyboard.press(Key.up)
                    keyboard.release(Key.up)
                    print("Pressed UP arrow key")
                # If value is between 98 and 127, press the down arrow key
                elif 98 <= msg.value <= 127:
                    keyboard.press(Key.down)
                    keyboard.release(Key.down)
                    print("Pressed DOWN arrow key")

if __name__ == "__main__":
    print_midi_input()
