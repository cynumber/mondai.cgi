#!/usr/bin/perl -w

print "Content-Type: text/html\n";
print "\n";
read(STDIN, $data, $ENV{'CONTENT_LENGTH'});
if(!-d"./$ENV{'HTTP_COOKIE'}"){
  mkdir"./$ENV{'HTTP_COOKIE'}";
}
open(OUT, ">./$ENV{'HTTP_COOKIE'}/$$.txt");
print $$, "\n";
print OUT $data;
close(OUT);
print "OK\n";
print $data;
