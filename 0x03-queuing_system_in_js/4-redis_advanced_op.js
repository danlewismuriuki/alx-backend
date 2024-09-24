import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
})

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});


function createHash() {
    const key = "HolbertonSchools";

    const values = {
        Portland: 50,
        Seattle: 80,
        'New York': 20,
        Bogota: 20,
        Cali: 40,
        Paris: 2
    };

    for (const [field, value] of Object.entries(values)) {
        client.hset(key, field, value, redis.print);
    }
    displayHash(key)
}

function displayHash(key) {
    client.hgetall(key, (err, reply) => {
        if (err) {
            console.error(`Error retrieving hash: ${err}`);
        } else {
            console.log(reply);
        }
    });
}

createHash()