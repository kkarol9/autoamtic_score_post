30.04

CEL: Stworzyc program który będzie pobierał wyniki ze strony sofascore (co 
dwie godziny, zakonczone mecze wrzucał do jednej np. listy, a te trwające 
do drugiej. Z zakonczonych meczy co 2h robi posty na instagrama który 
możesz sobie wrzucic.

Let's go!


Sledzic mecze ktore sa inprogress i jesli ich status zmieni sie na finished tworzyc post i jesli nazwisko == nazwisko klienta 
wrzucac go na instagrama.

7.05

Sprawdzam czy id meczu not started lub in progress jest w liscie:
jesli nie to go tam wrzucam
jesli tak to nic

sprawdzam czy nadal jest in progress lub not started
jesli sie zmienilo na finished
tworze post
usuwaam z listy

Czyli jeden program co dwie h dostarcza mi swieze dane. Sprawdzam, czy id tych meczow in progress badz not started sa na liscie... 



czyli mam 3 mecze
id1 not started
id2 in progress
id 3 finished

wszucam [id1, id2] do listy
sprawdzam status id 1, id2
jesli sie zmienil to tworze post i usuwam z listy
