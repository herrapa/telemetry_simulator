#include <Servo.h>

Servo s1;
Servo s2;
Servo s3;

int val;

int x;
int y;

union u_tag {
   byte b[4];
   float fval;
} u;

void setup()
{
  s1.attach(9);
  s2.attach(10);
  s3.attach(11);
  Serial.begin(115200);
}

void loop() 
{ 
  
  if (Serial.available() >= 8) {
    
    u.b[0] = Serial.read();
    u.b[1] = Serial.read();
    u.b[2] = Serial.read();
    u.b[3] = Serial.read();
    x = u.fval * 200.0; // 128
    
    u.b[0] = Serial.read();
    u.b[1] = Serial.read();
    u.b[2] = Serial.read();
    u.b[3] = Serial.read();
    y = u.fval * 200.0; // 128
  }
  val = analogRead(0);            // reads the value of the potentiometer (value between 0 and 1023) 
  val = map(val, 0, 1023, -700, 700);     // scale it to use it with the servo (value between 0 and 180) 
  s1.writeMicroseconds(1500 + val - y);
  s2.writeMicroseconds(1500 + val + y + x);
  s3.writeMicroseconds(1500 + val + y - x);
  //delay(15);
  //Serial.println(val);
} 

