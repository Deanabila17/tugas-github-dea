// Improved code
const int motorPin = 9;  // Pin for the motor
const int sensorPin = A0;  // Pin for the sensor
const int threshold = 500;  // Threshold value for the sensor
const int motorSpeedMax = 255;  // Maximum motor speed
const int timeout = 10000;  // Timeout in milliseconds

int sensorValue = 0;  // Sensor value
int motorSpeed = 0;  // Motor speed
unsigned long startTime = 0;  // Start time of the motor

void setup() {
  pinMode(motorPin, OUTPUT);
  pinMode(sensorPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // Read sensor value with median filter
  sensorValue = readSensorValue();
  
  // Calculate motor speed using PID controller
  motorSpeed = calculateMotorSpeed(sensorValue);
  
  // Limit motor speed
  motorSpeed = constrain(motorSpeed, 0, motorSpeedMax);
  
  // Update motor speed
  analogWrite(motorPin, motorSpeed);
  
  // Check for timeout
  if (millis() - startTime > timeout) {
    digitalWrite(motorPin, LOW);
  }
  
  delay(50);
}

// Function to read sensor value with median filter
int readSensorValue() {
  int values[5];
  for (int i = 0; i < 5; i++) {
    values[i] = analogRead(sensorPin);
    delay(10);
  }
  int medianValue = getMedian(values, 5);
  return medianValue;
}

// Function to calculate motor speed using PID controller
int calculateMotorSpeed(int sensorValue) {
  // TO DO: implement PID controller algorithm
  // For now, use a simple proportional controller
  int error = sensorValue - threshold;
  int motorSpeed = error * 2;
  return motorSpeed;
}

// Function to get the median value of an array
int getMedian(int values[], int size) {
  int medianValue;
  if (size % 2 == 0) {
    medianValue = (values[size / 2 - 1] + values[size / 2]) / 2;
  } else {
    medianValue = values[size / 2];
  }
  return medianValue;
}
