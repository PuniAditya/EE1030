#include <Wire.h>
#include <Adafruit_ADS1X15.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // RS, E, D4, D5, D6, D7
Adafruit_ADS1115 ads;

const float A_COEFF = 0.0155;
const float B_COEFF = -0.000112;

const int AVG_SAMPLES = 10;
float moving_avg[AVG_SAMPLES] = {0.0};
int idx = 0;

void setup() {
  Serial.begin(9600);
  ads.begin();
  ads.setGain(GAIN_ONE);
  lcd.begin(16, 2);
  lcd.clear();
  lcd.print("PT100 System");
}

void loop() {
  int16_t adc_raw = ads.readADC_Differential_0_1();
  float v_out = adc_raw * 0.1875 / 1000.0;
  
  float temp = 0.0;
  float discriminant = (A_COEFF * A_COEFF) - (4 * B_COEFF * (1.0 - v_out));
  
  if (discriminant >= 0) {
    temp = (-A_COEFF + sqrt(discriminant)) / (2.0 * B_COEFF);
  }
  
  moving_avg[idx] = temp;
  idx++;
  if(idx >= AVG_SAMPLES) {
    idx = 0;
  }
  
  float sum = 0.0;
  for(int i = 0; i < AVG_SAMPLES; i++) {
    sum += moving_avg[i];
  }
  float avg_temp = sum / AVG_SAMPLES;
  
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("V: ");
  lcd.print(v_out, 3);
  lcd.print(" V");

  lcd.setCursor(0, 1);
  lcd.print("Temp: ");
  lcd.print(avg_temp, 2);
  lcd.print((char)223);
  lcd.print("C");

  delay(1000);
}

