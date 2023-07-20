import redis from 'redis';

const publisher = redis.createClient();

publisher.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

publisher.on('ready', () => {
  console.log('Redis client connected to the server');
});

const CHANNEL = 'holberton school channel';

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish(CHANNEL, message);
  }, time);
}

publishMessage('Holberton Student #1 starts course', 1000);
publishMessage('Holberton Student #2 starts course', 2000);
publishMessage('KILL_SERVER', 3000);
