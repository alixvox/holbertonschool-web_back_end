import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('ready', () => {
  console.log('Redis client connected to the server');
});

// Create Hash
const hashKey = 'HolbertonSchools';
const hashValues = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2',
};

for (const [key, value] of Object.entries(hashValues)) {
  client.hset(hashKey, key, value, redis.print);
}

// Display Hash
client.hgetall(hashKey, (err, object) => {
  console.log(object);
});
