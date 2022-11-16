cd server
docker build -t server-image .
docker run --rm -it -p 9000:9000 --name server server-image

cd client
docker build -t client-image .
docker run --rm -it -p 3000:3000 --name client client-image