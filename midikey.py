import mido

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
            print(msg)

if __name__ == "__main__":
    print_midi_input()
