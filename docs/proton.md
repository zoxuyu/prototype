#PROTON CONVENTION 1.0.0
##Proton 1 - Zweck dieser Convention
Dies ist die Proton-Convention. Sie hat das Ziel, Prototype-Code einfacher lesbar und offener zu machen. Im allgemeinen gilt, dass Projektspezifische Conventions vorrang vor Proton haben. Obwohl die Engine bei manchen ausgelassenen Protonen nicht fehlschlagen wird, ist es doch empfohlen sich an Proton zu halten. Vorallem bei größeren Projekten mit mehreren Mitarbeitern und Code-Schnippsel-Teil-Webseiten ist es hilfreich gewisse Standards aufrecht zu erhalten. Darum wurde von der Prototype-Workgroup diese PROTON-CONVENTION erarbeitet.

Im folgenden werden Beispiele in Prototype und in Python auftreten. Die Schnittstellen und sonstige Namensbezeichungen werden auch in anderen Parsersprachen als Python so erhalten bleiben.
##Proton 2 - Begriffsklärung
**Prototype** ist eine von der Prototype-Workgroup entwickelte Programmiersprache. Diese sticht vor allem dadurch heraus, dass sie anders als die meisten anderen auch von außen her erweiterbar ist. Um diese Programmiersprache dreht sich die PROTON-CONVENTION.

Die **Engine** ist ein Programm, welches Prototype-Code aufnimmt, sich um die Variablenspeicherung kümmert und von den Parsern das Ergebnis verlangt. Die Engine selber führt keine Befehle aus sondern verwaltet Zuordnungen, Funktionen und die Einbindung der Parser.

Ein **Parser** ist ein Objekt, dass einen gewissen Satz von Befehlen verwaltet und diese bei Bedarf ausführt und das Ergebnis zurückgibt.
##Proton 3 - Aufbau von Programmen
Ein Prototype-Programm ist in mehrere Teile gegliedert. Als erstes folgt ein einleitender Kommentar, der erklärt was dieses Programm macht, sowie eine Urheberrechtserklärung.
```
? Beispielprogramm, Version 1.0.0
? (C) 2016 Mein Name, Lizensiert unter der GPL 123
```
Anschließend folgt nach einer Leerzeile die Einbindung der Parser. Zuvor jedoch ein Kommentar mit der Erklärung, dass hier die Parser eingebunden werden.
```
? Parser
#! vergiss.mein.nicht.v2-beta
#! lorem.ipsum.dolor.sit.amet.v1
```
Nach einer weiteren Leerzeile werden die Module eingebunden. Ebenso ein Hinweis auf die Moduleinbindung
```
? Module
Require "TicTacToe" from "tictactoe.mod.proto"
Require "ShingShangShong" from "scisserstonepaper.mod.proto"
```
##Proton 4 - Aufbau von Modulen
##Proton 5 - Code-Formattierung
##Proton 6 - Namensbezeichnungen
###6.1 - Bei Prototype-Programmen
###6.2 - Bei Prototype-Modulen
###6.3 - Bei Parsern
##Proton 7 - Die Parser-Interface
