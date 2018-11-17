#include <CapacitiveSensor.h>

/*
 * CapitiveSense Library Demo Sketch
 * Paul Badger 2008
 * Uses a high value resistor e.g. 10M between send pin and receive pin
 * Resistor effects sensitivity, experiment with values, 50K - 50M. Larger resistor values yield larger sensor values.
 * Receive pin is the sensor pin - try different amounts of foil/metal on this pin
 */
int del = 15; // delay between reads
 
int red = 10;
int green = 9;
int blue = 8;

boolean rOn = false;
boolean gOn = false;
boolean bOn = false;

int sendTreshhold = 200;
int capSenseMax1 = -1;
int valLen = 30;
//int *values1[valLen];
int *values1 = new int[valLen];

boolean shouldWriteVals1 = false;

CapacitiveSensor   cs_4_2 = CapacitiveSensor(4,2);        // 10M resistor between pins 4 & 2, pin 2 is sensor pin, add a wire and or foil if desired
//CapacitiveSensor   cs_4_6 = CapacitiveSensor(4,6);        // 10M resistor between pins 4 & 6, pin 6 is sensor pin, add a wire and or foil
//CapacitiveSensor   cs_4_8 = CapacitiveSensor(4,8);        // 10M resistor between pins 4 & 8, pin 8 is sensor pin, add a wire and or foil

void setup(){
   Serial.begin(9600);
   Serial1.begin(9600);
   //Serial.println("----- start -----");
   //cs_4_2.set_CS_AutocaL_Millis(0xFFFFFFFF);     // turn off autocalibrate on channel 1 - just as an example
   pinMode(red, OUTPUT);
   pinMode(green, OUTPUT);
   pinMode(blue, OUTPUT);
   pinMode(13, OUTPUT);
   digitalWrite(13, LOW);
   
}

void loop(){
    //Serial.print("=="); 
    long start = millis();
    long total1 =  cs_4_2.capacitiveSensor(30);
    //Serial.print(millis() - start);        // check on performance in milliseconds
    //Serial.print("\n");                    // tab character for debug windown spacing
    //Serial.println(total1);                  // print sensor output 1
    //Serial.print("\n");
    
    delay(del);                              // arbitrary delay to limit data to serial port 

    // set threshold value for sending readings
    if (capSenseMax1 == -1){
      if (!values1[valLen-1]) {
        int ind = getEmptyIndexOf(values1, valLen);
        values1[ind] = total1;
      } else {
        capSenseMax1 = getArrayMax(values1, valLen); //getArrayAvg(values);
        emptyArray(values1, valLen);
        //Serial.print("capSenseMax1s ");
        //Serial.println(capSenseMax1);
      }
    }
    
    
    
    // open gate to vals storage
    if (shouldWriteVals1==false && total1 > (capSenseMax1 + sendTreshhold)){
      //Serial.println("should write");
      shouldWriteVals1 = true;
    }
    
    // store sensor vals
    if (shouldWriteVals1){
      int ind = getEmptyIndexOf(values1, valLen);
      values1[ind] = total1;
      // end writing to vals
      if (ind==valLen-1) {
        shouldWriteVals1 = false;
        printVals(values1, valLen);
        emptyArray(values1, valLen);
      }
    }

    // read incoming stuff/ gesture classes
    int led = 0;
    char currLab = 'q';
    
    // read serial = class of gesture
    while (Serial.available() > 0) {
      //Serial.println("ava");
      String result = Serial.readString();
      currLab = result[0];
      //Serial.println(currLab);
    }
    if      (currLab == 'a') led = red;
    else if (currLab == 'b') led = green;
    else if (currLab == 'c') led = blue;
    //else Serial.println("none");
    
    if (led>0) {
      if (led == 10){
        if (!rOn){ 
            rOn = true;
            digitalWrite(led, HIGH);
        } else {
            rOn = false;
            digitalWrite(led, LOW);
        }
      } else if(led == 9){
        if (!gOn){ 
            gOn = true;
            digitalWrite(led, HIGH);
        } else {
            gOn = false;
            digitalWrite(led, LOW);
        }
      } else if(led == 8){
        if (!bOn){ 
            bOn = true;
            digitalWrite(led, HIGH);
        } else {
            bOn = false;
            digitalWrite(led, LOW);
        }
      }
      //delay(500);
      //digitalWrite(led, LOW);
    }
    //currLab = 'q';
}

void blink13(int del){
  digitalWrite(13, HIGH);
  delay(50);
  digitalWrite(13, LOW);
}

// memory management
// https://www.arduino.cc/reference/en/language/variables/utilities/progmem/

void printVals(int vals[30], int valLen){
  Serial.print("[");
  for (int i=0; i < valLen; i++){
    Serial.print(vals[i]);
    if (i<valLen-1) Serial.print(",");
  }
  //Serial.println(" ");
  Serial.println("]");
}


void emptyArray(int vals[30], int valLen){
  for (int i=0; i<valLen; i++){
    vals[i] = 0;
  }
}



int getArrayMax(int vals[30], int valLen){
    int maxim = -1;
    for (int i=0; i<valLen; i++){
      if (vals[i]>maxim) maxim = vals[i];
    }
    return maxim;
}

float getArrayAvg(int vals[30], int valLen){
    float sum = 0.0;
    for (int i=0; i<valLen; i++){
      sum = sum + vals[i];
    }
    return sum/valLen;
}

int getEmptyIndexOf(int vals[30], int valLen){
    int result = -1;
    for (int i=0; i< valLen, result=-1; i++){
      if (!vals[i]) return i;
    }
    return result;
}
