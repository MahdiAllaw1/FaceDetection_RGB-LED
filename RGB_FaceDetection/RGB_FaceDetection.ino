#include <cvzone.h>

SerialData serialData(3,1);
int valRec[3];

int red = 3;
int green = 5;
int blue = 6;

void setup() {
  serialData.begin();
  pinMode(red, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(green, OUTPUT);

}

void loop() 
{
  serialData.Get(valRec);
  
  digitalWrite(red, valRec[0]);
  digitalWrite(green, valRec[1]);
  digitalWrite(blue, valRec[2]);

}
