from deep_translator import GoogleTranslator
def translate_ar(msg):
    if msg.startswith(">>tr "):
      tr =GoogleTranslator(source='auto', target='ar').translate(msg[5:])
    elif msg.startswith(">>translate "):
      tr =GoogleTranslator(source='auto', target='ar').translate(msg[12:])
    return tr


def translate_en(msg):
    if msg.startswith(">>tr "):
      tr =GoogleTranslator(source='auto', target='en').translate(msg[5:])
    elif msg.startswith(">>translate "):
      tr =GoogleTranslator(source='auto', target='en').translate(msg[12:])
    return tr

def translate_ar0(msg):
    tr =GoogleTranslator(source='auto', target='ar').translate(msg)
    return tr

def translate_en0(msg):
    tr =GoogleTranslator(source='auto', target='en').translate(msg)
    return tr