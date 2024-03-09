#!/usr/bin/perl

$someString = "Hello";

print "$someString, world!\n";

@someChars = ("H", "i", "!", "\n");

print "@someChars $someChars[3]";

%moreData = ('one', 1, 'two', 2, 'three', 3);

print "Number: $moreData{'two'}\n";

$ts = "T" x 5;

print "Ts: $ts"
