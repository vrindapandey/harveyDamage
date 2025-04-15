
how to start inference server:/n
docker compose up\n
docker compose down 

compose file: docker-compose.yml
image name: model-inference-server

how to curl command: 
curl -X POST http://172.17.0.3:5000/inference -F "image=@data/damage/-93.66109_30.212114.jpeg"

