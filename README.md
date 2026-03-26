docker-compose up -d
up: Starts the services defined in the file.

-d: Stands for "Detached" mode. It runs Kafka in the background so it doesn't lock up your terminal window.

docker ps 
up good
running restart

docker exec -it kafka /usr/bin/kafka-topics --create --topic iss-tracking --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1