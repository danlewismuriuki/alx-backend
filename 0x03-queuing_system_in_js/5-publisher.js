import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('connect', (err, error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

function publishMessage(message, time) {
    setTimeout(() => {
        if (time === time(time)) {
            console.log('About to send MESSAGE');
        }
    })
};