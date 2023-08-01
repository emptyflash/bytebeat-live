python3 bytebeat.py 2>error.log > >(aplay -c 2 -f S16_LE -D hw:1,0) &
echo $! > bytebeat.pid
