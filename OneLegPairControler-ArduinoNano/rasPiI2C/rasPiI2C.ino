/* 
 * Arduino code to send and receive I2C data
 * Tested on Adafruit Feather M0+ Express and Raspberry Pi Model 4
 * 
 * SDA <--> SDA
 * SCL <--> SCL
 * GND <--> GND
 * 
 * Sets built-in LED (1 = on, 0 = off) on Feather when requested 
 * and responds with data received
 */
#include <Wire.h>
#define SLAVE_ADDRESS 0x04       // I2C address for Arduino
#define LED 13                   // Built-in LED
int i2cData = 0;                 // the I2C data received
void setup(){
  Serial.begin(115200);

  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);
}
void loop() {
  // Everything happens in the interrupts
}
// Handle reception of incoming I2C data
void receiveData(int byteCount) {
  while (Wire.available()) {
    i2cData = Wire.read();

  }
}
// Handle request to send I2C data
void sendData() { 
  Wire.write(1);
  Serial.write('1');
  Wire.write(2);
  Serial.write('2');
  Wire.write(3);
  Serial.write('3');
  Wire.write(i2cData);
  Serial.write(int(i2cData));
  Wire.write(3);
  Serial.write('3');
  Wire.write(2);
  Serial.write('2');
  Wire.write(1);
  Serial.write('1');
  Serial.write(char(10));
  Serial.write(char(13));
}