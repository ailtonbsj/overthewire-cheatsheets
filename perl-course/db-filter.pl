#!/usr/bin/perl

# Using Perl on XAMPP provided by SECITIF Docker Containers
# Details in: https://github.com/ailtonbsj/secitif

use CGI qw(:standard);
use DBI;

$dsn = "DBI:mysql:database=secitif_demo;host=127.0.0.1";
$user = "root";
$pass = "";
$dbh = DBI->connect($dsn, $user, $pass) or die $DBI::errstr;
print("Content-Type: text/html\n\n<pre>");

if('GET' eq request_method && param('pass') && param('user')) {
   print("Select * FROM users where username =".$dbh->quote(param('user')) . " and password =".$dbh->quote(param('pass')));
}

print("\n\nFinished!</pre>\n");
