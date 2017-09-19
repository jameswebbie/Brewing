#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2
#define RELAY_SWITCH 4
OneWire oneWire(ONE_WIRE_BUS);

DallasTemperature sensors(&oneWire);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(RELAY_SWITCH, OUTPUT);
  sensors.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  sensors.requestTemperatures();
  double temp = 0;
  temp = sensors.getTempCByIndex(0);

  if (temp > 65) {
  digitalWrite(RELAY_SWITCH, LOW);

  } else if (temp < 60) {
  digitalWrite(RELAY_SWITCH, HIGH);

  }

  Serial.print("Temp is ");
  Serial.println(temp);
  delay(1000);
}
