# Start the camera
mkdir /tmp/stream
raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &
# start MJPG-Streamer
LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w /usr/local/www"
# Watch the stream
#Now you can connect with your web browser and watch the stream live. If you want to watch from within the same Raspberry Pi you can enter http://localhost:8080 in the browser's address bar. If you want to watch from another computer in your network use http://<IP-address>:8080.

#cleanup
#cd ../../
#rm -rf mjpg-streamer-182
