## Regular expression
```
echo 'data' | sed 's/[ab]//g' 
>> dt

echo 'data' | sed 's/[ab]//'
>> dta

echo 'dabta' | sed 's/(ab)*//g'
>> dta (replace ab with none elements)

echo 'dabcta' | sed 's/(ab|bc)*//g' (alternative removing)
>> dcta

```
## other tools

sort, uniq -c, awk, paste -sd, bc -l, gnuplot -p -e, xargs (turn lines into arguments)

```
xargs rustup toolchain unintall (will run the rustup toolchain uninstall ...)

ffmpeg -loglevel panic -i /dev/video/... -frames 1 -f image2 - | convert - -colorspace gray | gzip | ssh ...(to the server)
```