#include <IRLibAll.h>

IRsend mySender;

void setup() {
  Serial.begin(9600);
}

void loop() {
  char c = Serial.read();
  if (c != -1) {
    switch (c) {
      case '+':
        mySender.send(NEC,0x4BB640BF, 32);
        break; 
      case '-':
        mySender.send(NEC,0x4BB6C03F, 32);
        break;
      case 'r':
        mySender.send(NEC,0xFF906F, 32);
        break;
      case 't':
        mySender.send(NEC,0xFF50AF, 32);
        break;
    }
    Serial.write(c);
  }
}
