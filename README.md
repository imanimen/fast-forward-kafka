# Create test topic
`docker compose exec kafka /opt/kafka/bin/kafka-topics.sh --create --topic test --bootstrap-server localhost:9092`

# Partitions `feature/partitions`
    # Create Topic on kafka
    docker compose exec kafka /opt/kafka/bin/kafka-topics.sh --create --topic orders 3 --bootstrap-server localhost:9092

    # Run the producer (1 Terminal)
    uv run producer.py
    # Run the consumer (3 Terminals) (because we have 3 partitions)
    uv run consumer.py
