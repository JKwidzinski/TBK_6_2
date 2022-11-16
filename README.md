cd server<br />
docker build -t server-image .<br />
docker run --rm -it -p 9000:9000 --name server server-image<br />
<br />
cd client<br />
docker build -t client-image .<br />
docker run --rm -it -p 3000:3000 --name client client-image<br />
