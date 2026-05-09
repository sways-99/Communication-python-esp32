int ledA = 2;
int ledR = 5;
int ledV = 4;

void setup() {
 Serial.begin(9600);
 pinMode(ledA, OUTPUT);
 pinMode(ledR, OUTPUT);
 pinMode(ledV, OUTPUT);

}

void loop() {
  if (Serial.available()){

    char dato = Serial.read();

    digitalWrite(ledA, LOW);
    digitalWrite(ledR, LOW);
    digitalWrite(ledV, LOW);


    //LED AZUL
   if (dato == 'A'){
      digitalWrite(ledA, HIGH);
    }
    else if (dato == 'R'){
      digitalWrite(ledR, HIGH);
    }
    else if(dato == 'V'){
      digitalWrite(ledV, HIGH);
    }

  }

}
