#include <wiringPi.h>
#define RED 2
#define YELLOW 3
#define GREEN 4
int main (void)
{
  // wiringPiSetup();
  wiringPiSetupGpio();
  pinMode (RED, OUTPUT);
  pinMode (YELLOW, OUTPUT);
  pinMode (GREEN, OUTPUT);

  digitalWrite (RED, HIGH); delay (2000);
  digitalWrite (RED,  LOW);
  digitalWrite (YELLOW, HIGH); delay (2000);
  digitalWrite (YELLOW,  LOW);
  digitalWrite (GREEN, HIGH); delay (2000);
  digitalWrite (GREEN,  LOW);

  pinMode (RED, INPUT);
  pinMode (YELLOW, INPUT);
  pinMode (GREEN, INPUT);

  return 0;
}