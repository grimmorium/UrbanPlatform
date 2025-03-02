#include <Wire.h>
#define SLAVE_ADDRESS 0x04       // I2C address for Arduino
int i2cData = 0;                 // the I2C data received

char charAr[11];

byte charCnt = -1;

char msgType = ' ';

short AdjS1=0;
short AdjS2=0;
short AdjS3=0;
short AdjS4=0;
short AdjS5=0;
short AdjS6=0;
short AdjDC=0;

byte S1=180;
byte S2=180;
byte S3=180;
byte S4=180;
byte S5=180;
byte S6=180;
byte DC=180;

void setup(){
  Serial.begin(115200);

  Wire.begin(SLAVE_ADDRESS);
  Wire.setWireTimeout(200,false);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
}
void loop() {
  // Everything happens in the interrupts
}
// Handle reception of incoming I2C data
void receiveData(int byteCount) {

  
  while (Wire.available()) {
    i2cData = Wire.read();
    if(i2cData == '<'){charCnt = 1;}
    if(charCnt = 2){msgType = i2cData;}

    if(charCnt = 3){S1 = i2cData;}
    if(charCnt = 4){S2 = i2cData;}
    if(charCnt = 5){S3 = i2cData;}
    if(charCnt = 6){S4 = i2cData;}
    if(charCnt = 7){S5 = i2cData;}
    if(charCnt = 8){S6 = i2cData;}
    if(charCnt = 9){DC = i2cData;}

    if(i2cData == '>'){charCnt = -1; setMotoServoStates();}
    if(charCnt > 1){charCnt++;}
    
  }
  
}

void setMotoServoStates(){
  Serial.print(msgType);
  Serial.print(" - ");
  Serial.println("setMotoServoStates IN");

  msgType = ' ';
  AdjS1=0;
  AdjS2=0;
  AdjS3=0;
  AdjS4=0;
  AdjS5=0;
  AdjS6=0;
  AdjDC=0;
  S1=180;
  S2=180;
  S3=180;
  S4=180;
  S5=180;
  S6=180;
  DC=0;
}

// Handle request to send I2C data
void sendData() { 

  //Serial.write(char(10));
  //Serial.write(char(13));
}