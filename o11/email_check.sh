#!/bin/bash

function recursive_lookup() {

  if [ "$1" = "" ]
  then
    return
  fi

  spf_lookup=$(nslookup -type=txt $1 | grep ".*spf1.*" | cut -f 2 )
  for string in $spf_lookup
  do
    if [[ $string =~ include:.* ]]
    then
     echo $string | cut -d ":" -f 2
     recursive_lookup $(echo $string | cut -d ":" -f 2)
    fi
  if [[ $string =~ redirect=.* ]]
  then
   echo echo $string | cut -d "=" -f 2 | cut -d "\"" -f 1
   recursive_lookup $(echo $string | cut -d "=" -f 2 | cut -d "\"" -f 1)
  fi
  done
  return
}

target=$@
echo ---"Scanning "$target---
domain=$(nslookup $target | grep "Name:.*" | cut -f 2)
ips=$(nslookup $target | grep "Address:.*" | cut -f 3)

ipv4s=""
ipv6s=""
for string in $ips
do
  if [[ "$string" != "Address:" ]];
  then
    if [[ $string =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]];
    then
      ipv4s="$ipv4s $string"
    else
      ipv6s="$ipv6s $string"
    fi
  fi
done

echo "domain names: "$domain
echo "ipv4s: "$ipv4s
echo "ipv6s: "$ipv6s
echo
echo "---reverse lookup---"
for string in $ipv4s $ipv6s
do
  addr_domain=$(nslookup $string | grep ".*name = .*" | cut -d "=" -f 2)

  if [[ $addr_domain == "" ]];
  then
    addr_domain="None found"
  fi

  echo "Reverse lookup of $string: " $addr_domain
done

echo
echo "---mx servers---"
mx_servers=$(nslookup -type=mx $@ | grep ".*mail exchanger.*" | cut -d "=" -f 2)

for string in $mx_servers
do
  if ! [[ $string =~ ^[0-9]+$ ]]
  then
    echo $string
  fi
done

echo
echo "---spf lookup---"
spf_lookup=$(nslookup -type=txt $@ | grep ".*spf1.*" | cut -f 2 )
if [[ $spf_lookup == "" ]]
then
  echo None found
  exit 0
fi


for string in $spf_lookup
do
  if [[ $string =~ include:.* ]]
  then
   echo $string | cut -d ":" -f 2
   recursive_lookup $(echo $string | cut -d ":" -f 2)
  fi
  if [[ $string =~ redirect=.* ]]
  then
    echo $string | cut -d "=" -f 2 | cut -d "\"" -f 1
    recursive_lookup $(echo $string | cut -d "=" -f 2 | cut -d "\"" -f 1)
  fi

done