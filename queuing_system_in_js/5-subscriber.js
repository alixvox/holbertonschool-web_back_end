import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

subscriber.on('ready', () => {
  console.log('Redis client connected to the server');
});

const CHANNEL = 'holberton school channel';

subscriber.subscribe(CHANNEL);

subscriber.on('message', (channel, message) => {
  console.log(message);

  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
