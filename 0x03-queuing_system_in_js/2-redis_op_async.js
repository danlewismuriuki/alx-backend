import redis from 'redis';
import { promisfy } from 'util';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server')
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

const getAsync = promisfy(client.get).bind(client);

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName)
        console.log(value);
    } catch (err) {
        console.error(`Error retrieving value for ${schoolName}: ${err}`)
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');