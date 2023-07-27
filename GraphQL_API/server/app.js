const cors = require('cors');
const express = require('express');
const {graphqlHTTP} = require('express-graphql');
const schema = require('./schema/schema');
const mongoose = require('mongoose');

//Mongodb connection string
const uri = 'mongodb+srv://alixvox:hncPjfDjMymIHnbq@cluster0.6owjuif.mongodb.net/?retryWrites=true&w=majority'

const app = express();
app.use(cors());

mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });
mongoose.connection.once('open', () => {
    console.log('connected to database');
});

app.use('/graphql',graphqlHTTP({
    schema,
    graphiql: true
}));

app.listen(4000, () => {
  console.log('now listening for request on port 4000');
});
