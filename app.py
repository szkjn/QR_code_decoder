import cv2
import webbrowser as wb
from pyzbar import pyzbar

global qrcode_in_memory
global img_counter
qrcode_in_memory = ""
img_counter = 0

def display_text(frame, text, x, y):
  fontface = cv2.FONT_HERSHEY_SIMPLEX
  font_scale = .7
  thickness = 1

  textSize = cv2.getTextSize(text, fontface, font_scale, thickness)
  dimension = textSize[0]
  baseline = textSize[1]

  cv2.rectangle(frame, (x - 5, y - 5), (x + dimension[0], y + dimension[1] + baseline), (0, 0, 0), cv2.FILLED)
  cv2.putText(frame, text, (x, y + dimension[1]), fontface, font_scale, (0, 255, 0), thickness, cv2.LINE_AA)

def qrcode_decoder(frame):

  global qrcode_in_memory
  decoded = pyzbar.decode(frame)

  if decoded != []:
    if decoded[0].type == 'QRCODE':
      qrcode = decoded[0]
      x, y , w, h = qrcode.rect
      qrcode_text = qrcode.data.decode('utf-8')
      if qrcode_text == qrcode_in_memory:
        pass
      elif "https://" in qrcode_text:
        wb.open_new_tab(qrcode_text)
        qrcode_in_memory = qrcode_text
      else:
        content = qrcode.data.decode('utf-8')
        display_text(frame, content, 20, 20)
      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
  return frame

def feed():
  global img_counter
  cam = cv2.VideoCapture(0)
  instructions = "Press (q) to (q)uit, (s) to (s)ave picture"

  while True:
    _, frame = cam.read()
    frame = qrcode_decoder(frame)
    display_text(frame, instructions, 20, 450)
    cv2.imshow('QR Decoder', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    elif cv2.waitKey(1) & 0xFF == ord('s'):
      img_name = "opencv_frame_{}.png".format(img_counter)
      cv2.imwrite(img_name, frame)
      print("{} image saved.".format(img_name))
      img_counter += 1

  cam.release()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  feed()