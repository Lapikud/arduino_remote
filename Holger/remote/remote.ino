#include <IRLibAll.h>

IRsend mySender;

void setup() {
  Serial.begin(9600);
}

void loop() {
  char c = Serial.read();
  if (c != -1) {
    switch (c) {
      case 'm':
        mySender.send(NEC,0x0AA1, 12);
        break;
      case 'r':
        mySender.send(NEC,0xFF906F, 32);
        break;
      case 't':
        mySender.send(NEC,0xFF50AF, 32);
        break;
       case 'l':
        mySender.send(NEC,0xFFF00F, 32);  // blink
        break;
       case 'q':
        mySender.send(NEC,0x4BB640B, 32); // vol +
        break;
       case 'w':
        mySender.send(NEC,0x4BB6C03F, 32); // vol -
        break;
    }
    Serial.write(c);
  }
}
