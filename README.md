#Prototype
##Was ist das?
Prototype ist eine Programmiersprache, die durch ihre Einfachkeit und Flexibilität heraussticht
##Syntax
Die ersten Zeilen bestehen, außer bei Modulen, immer aus einer Parserangabe. Diese hält sich meistens an folgendes muster:
```
#! <hersteller>.<package>(.<subpackage).v<versionsnummer>
```
Anschließend folgt ein eventuelles Include von Modulen, welches folgendermaßen aufgebaut ist.
```
Require "<Programmname>" from "<Dateiname>"
```
Dabei ist <Programmname> der Name des Programms, der im folgenden Angegeben wird.
```
Program "<Programmname>"
```
Anschließend folgt, eingerückt mit je vier Leerzeichen, der eigentliche Programmcode. Dabei ist es möglich Variablen zu definieren. Dazu nimmt man folgende Syntax:
```
<type={string|num|bool|list}>: <name> = <Zuordnung>
```
Auch If-Abfragen sind natürlich möglich. Der Code nach einer If-Abfrage wird um weitere vier stellen eingerückt.
```
If (<Bedingung>)
  ... <Code> ...
EndIf
```
Es gibt folgende Operatoren:

Operator | Bedeutung
-------- | ---------
>> | größer als
<< | kleiner als
== | gleich
a + b | a plus b
a - b | a minus b
a * b | a mal b
a / b | a durch b
a % b | a modulo b (Rest)
a ** b | a hoch b
n $ a | n-te Wurzel von a (=>  a ** (1/n))

Arrays sind folgendermaßen möglich:
```
list: <name> = [<element>, <element>, <...>]
```

Eine Umwandlung von Typen ist folgendermaßen möglich:
```
<neuer-typ>: <name> = <name> !<neuer-typ>
```

##Beispiel
```
#! zoxuyu.prototype.v1
#! zoxuyu.zero
Program "Syntax-Beispiel"
  string: Test = "Hallo Welt!"
  num: Zahl = 3.25
  Write {"Die Variable Test enthält: <Test>. Die Variable Zahl enthält: <Zahl>"}
  If (<Zahl> >> 3)
    Write {"<Zahl> ist größer als 3"}
  EndIf
EndProgram
```
Führt zu folgendem Ergebnis:
```
VAR:
----
string: Test = "Hallo Welt!"
num: Zahl = 3.25
AUSGABE:
--------
"Die Variable Test enthält: Hallo Welt!. Die Variable Zahl enthält: 3.25"
"3.25 ist größer als 3"
```
