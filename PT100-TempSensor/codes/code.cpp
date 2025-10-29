#include <Wire.h>
#include <Adafruit_ADS1X15.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // RS, E, D4, D5, D6, D7

Adafruit_ADS1115 ads;
const float ADC_MULTIPLIER_MV = 0.1875F;

const float V_IN = 5.0;
const float R_REF = 100.0;

const float R0 = 100.0;
const float A = 3.9083e-3;
const float B = -5.775e-7;

float moving_avg[10] = {0.0};
int idx = 0;

void setup() {
  Serial.begin(9600);
  ads.begin();
  ads.setGain(GAIN_TWOTHIRDS);
  lcd.begin(16, 2);
  lcd.clear();
}

void loop() {
  int16_t adc_raw = ads.readADC_Differential_0_1();
  float v_out = adc_raw*0.0001875 - 0.04671;
  if(idx == 10)
    idx = 0;
  moving_avg[idx++] = (v_out-2.598)/0.00318; 
  float sum = 0.0;
  for(int i = 0; i<10; i++)
    sum += moving_avg[i];
  lcd.clear();
  lcd.println(v_out, 4);
  lcd.println(sum/10, 2);

  delay(1000);
}