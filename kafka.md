Notes

- requires java and zookeeper
- article on running kafka on docker -- http://blog.jaceklaskowski.pl/2015/07/14/apache-kafka-on-docker.html

```
sudo apt-get install zookeeperd
useradd kafka -m
passwd kafka
adduser kafka sudo
```

Testing if Zookeer is running: `telnet localhost 2181`

enter: ruok

ZooKeeper will say imok and end the Telnet session.

```
wget "http://mirror.cc.columbia.edu/pub/software/apache/kafka/0.8.2.1/kafka_2.11-0.8.2.1.tgz" -O ~/Downloads/kafka.tgz
mkdir -p ~/kafka && cd ~/kafka
tar -xvzf ~/Downloads/kafka.tgz --strip 1
```

edit server.properties and add the following to enable topic deletion:

```
delete.topic.enable = true
```

```
nohup ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties > ~/kafka/kafka.log 2>&1 &
```

check ~/kafka/kafka.log for "INFO New leader..." text

Testing Kafka

```
echo "Hello, World" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic TutorialTopic > /dev/null
~/kafka/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic TutorialTopic --from-beginning
```
